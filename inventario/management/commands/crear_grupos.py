from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from inventario.models import Producto, Categoria


class Command(BaseCommand):
    help = 'Crea los grupos Administrador y Asistente con sus permisos, y usuarios de prueba'

    def handle(self, *args, **options):
        # Crear grupos
        grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
        grupo_asistente, _ = Group.objects.get_or_create(name='Asistente')

        # Permisos sobre Producto
        ct_producto = ContentType.objects.get_for_model(Producto)
        permisos = Permission.objects.filter(content_type=ct_producto)

        # Admin: todos los permisos (C-R-U-D)
        grupo_admin.permissions.set(permisos)
        # Asistente: solo lectura (view)
        perm_view = Permission.objects.get(codename='view_producto', content_type=ct_producto)
        grupo_asistente.permissions.set([perm_view])

        # Crear usuarios de prueba
        user_admin, created = User.objects.get_or_create(username='admin_tech', defaults={'is_staff': True})
        if created:
            user_admin.set_password('Admin1234!')
            user_admin.save()
        user_admin.groups.set([grupo_admin])

        user_asist, created = User.objects.get_or_create(username='asistente_tech', defaults={'is_staff': True})
        if created:
            user_asist.set_password('Asist1234!')
            user_asist.save()
        user_asist.groups.set([grupo_asistente])

        # Datos de prueba: categorías y productos
        cat1, _ = Categoria.objects.get_or_create(nombre='Notebooks', defaults={'descripcion': 'Equipos portátiles'})
        cat2, _ = Categoria.objects.get_or_create(nombre='Smartphones', defaults={'descripcion': 'Teléfonos móviles'})
        cat3, _ = Categoria.objects.get_or_create(nombre='Periféricos', defaults={'descripcion': 'Accesorios'})

        if not Producto.objects.exists():
            Producto.objects.bulk_create([
                Producto(nombre='Lenovo ThinkPad X1', categoria=cat1, precio=1200000, stock=10, sku='NB-001'),
                Producto(nombre='HP Pavilion 15', categoria=cat1, precio=650000, stock=15, sku='NB-002'),
                Producto(nombre='iPhone 15 Pro', categoria=cat2, precio=1100000, stock=8, sku='SP-001'),
                Producto(nombre='Samsung Galaxy S24', categoria=cat2, precio=900000, stock=12, sku='SP-002'),
                Producto(nombre='Teclado Logitech MX', categoria=cat3, precio=85000, stock=25, sku='PF-001'),
                Producto(nombre='Mouse Razer DeathAdder', categoria=cat3, precio=55000, stock=30, sku='PF-002'),
            ])
            self.stdout.write(self.style.SUCCESS('✅ Productos de prueba creados'))

        self.stdout.write(self.style.SUCCESS('✅ Grupos y usuarios creados correctamente'))
        self.stdout.write(self.style.SUCCESS('👤 admin_tech / Admin1234!'))
        self.stdout.write(self.style.SUCCESS('👤 asistente_tech / Asist1234!'))