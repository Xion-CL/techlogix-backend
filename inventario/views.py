from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Producto, Categoria
from .forms import ProductoForm
from .mixins import AdminRequiredMixin, AsistenteOrAdminRequiredMixin
from django.views import View


# ==================== VISTAS PÚBLICAS ====================

def index(request):
    """Template 1 - Inicio (Público)"""
    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    return render(request, 'index.html', {
        'total_productos': total_productos,
        'total_categorias': total_categorias
    })


def catalogo(request):
    """Template 2 - Catálogo público con filtros y búsqueda"""
    productos = Producto.objects.select_related('categoria').all()
    categorias = Categoria.objects.all()

    # Filtro por categoría
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Búsqueda por nombre
    busqueda = request.GET.get('busqueda')
    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) | Q(sku__icontains=busqueda)
        )

    return render(request, 'catalogo.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_actual': categoria_id,
        'busqueda': busqueda or ''
    })


# ==================== AUTENTICACIÓN ====================

def login_view(request):
    """Login personalizado con protección CSRF"""
    if request.user.is_authenticated:
        return redirect('admin_panel')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('admin_panel')
        else:
            messages.error(request, 'Credenciales inválidas')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente')
    return redirect('index')


# ==================== PANEL ADMINISTRATIVO ====================

class AdminPanelView(AsistenteOrAdminRequiredMixin, View):
    """Template 3 - Panel administrativo (Read para ambos roles)"""
    def get(self, request):
        productos = Producto.objects.select_related('categoria').all()
        es_admin = request.user.groups.filter(name='Administrador').exists()
        return render(request, 'admin_panel.html', {
            'productos': productos,
            'es_admin': es_admin
        })


# ==================== CRUD (Solo Administrador) ====================

class ProductoCreateView(AdminRequiredMixin, View):
    """CREATE - Crear producto"""
    def get(self, request):
        form = ProductoForm()
        return render(request, 'producto_form.html', {'form': form, 'accion': 'Crear'})

    def post(self, request):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('admin_panel')
        return render(request, 'producto_form.html', {'form': form, 'accion': 'Crear'})


class ProductoUpdateView(AdminRequiredMixin, View):
    """UPDATE - Editar producto"""
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(instance=producto)
        return render(request, 'producto_form.html', {'form': form, 'accion': 'Editar', 'producto': producto})

    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('admin_panel')
        return render(request, 'producto_form.html', {'form': form, 'accion': 'Editar', 'producto': producto})


class ProductoDeleteView(AdminRequiredMixin, View):
    """DELETE - Confirmar y eliminar producto"""
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        return render(request, 'producto_confirm_delete.html', {'producto': producto})

    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('admin_panel')


class ProductoDetailView(AsistenteOrAdminRequiredMixin, View):
    """READ - Detalle de producto"""
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        es_admin = request.user.groups.filter(name='Administrador').exists()
        return render(request, 'producto_detail.html', {
            'producto': producto,
            'es_admin': es_admin
        })