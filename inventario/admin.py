from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Criterio 2.1.2 - Personalización completa
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'sku', 'fecha_ingreso')
    list_filter = ('categoria', 'fecha_ingreso')
    search_fields = ('nombre', 'sku', 'categoria__nombre')
    list_per_page = 20
    ordering = ('-fecha_ingreso',)