from django.urls import path
from django.contrib import admin
from .views import TiposUsuariosView, UsuariosView, AdministradoresListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas para TiposUsuarios
    path('tipos-usuarios/', TiposUsuariosView.as_view(),name='tipos-usuarios-list'),
    path('tipos-usuarios/<int:pk>/', TiposUsuariosView.as_view(),name='tipos-usuarios-detail'),

    # Rutas para Usuarios
    path('usuarios/', UsuariosView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuariosView.as_view(), name='usuarios-detail'),

    # Ruta para listar administradores
    path('administradores/', AdministradoresListView.as_view(), name='administradores-list'),
]
