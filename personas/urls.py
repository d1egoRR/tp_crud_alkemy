from django.urls import path

from . import views

urlpatterns = [
    path('listado/', views.listado_cliente, name='listado_cliente'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
]
