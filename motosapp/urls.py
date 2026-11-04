from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_pagina, name='login_pagina'),
    path('motos/', views.lista_motos, name='lista_motos'),
    path('moto/<int:pk>/', views.detalle_moto, name='detalle_moto'),
    path('moto/nueva/', views.crear_moto, name='crear_moto'),
    path('moto/<int:pk>/editar/', views.editar_moto, name='editar_moto'),
    path('moto/<int:pk>/eliminar/', views.eliminar_moto, name='eliminar_moto'),
    
    path('api/login/', views.LoginAPIView.as_view(), name='login_api'),
    path('api/motos/', views.MotosAPIView.as_view(), name='api_motos'),
    path('api/motos/<int:id>/', views.MotoDetalleAPIView.as_view(), name ='api_moto_detalle'),    
]

