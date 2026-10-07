from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motos, name='lista_motos'),
    path('moto/<int:pk>/', views.detalle_moto, name='detalle_moto'),
    path('moto/nueva/', views.crear_moto, name='crear_moto'),
]