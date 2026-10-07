from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin: Solo usuarios del grupo 'Administrador' pueden acceder (C-U-D)"""
    login_url = 'login'

    def test_func(self):
        return self.request.user.groups.filter(name='Administrador').exists()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("Solo los Administradores pueden realizar esta acción.")
        return super().handle_no_permission()


class AsistenteOrAdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin: Usuarios de los grupos 'Administrador' o 'Asistente' pueden acceder (Read)"""
    login_url = 'login'

    def test_func(self):
        user = self.request.user
        return user.groups.filter(name__in=['Administrador', 'Asistente']).exists()

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied("No tienes permisos para acceder a esta sección.")
        return super().handle_no_permission()