from django.urls import path
from . import views

urlpatterns = [
    # Públicas
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Panel administrativo (Read)
    path('admin-panel/', views.AdminPanelView.as_view(), name='admin_panel'),

    # CRUD (Solo Administrador)
    path('producto/nuevo/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
]