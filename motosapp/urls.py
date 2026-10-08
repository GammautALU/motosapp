from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motos, name='lista_motos'),
    path('moto/<int:pk>/', views.detalle_moto, name='detalle_moto'),
    path('moto/nueva/', views.crear_moto, name='crear_moto'),
    path('moto/<int:pk>/editar/', views.editar_moto, name='editar_moto'),
    path('moto/<int:pk>/eliminar/', views.eliminar_moto, name='eliminar_moto'),
]

