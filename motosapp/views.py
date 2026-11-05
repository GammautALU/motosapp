from django.shortcuts import render, redirect, get_object_or_404
from .models import Moto
from .forms import MotoForm

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# READ (Lista principal)
def lista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motosapp/lista_motos.html', {'motos': motos})

# READ (Detalle)
def detalle_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    return render(request, 'motosapp/detalle_moto.html', {'moto': moto})

# CREATE (Crear)
def crear_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotoForm()
    return render(request, 'motosapp/crear_moto.html', {'form': form})

from .forms import MotoForm, MotoEditarForm

# UPDATE
def editar_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        form = MotoEditarForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotoEditarForm(instance=moto)
    return render(request, 'motosapp/editar_moto.html', {'form': form, 'moto': moto})

# DELETE
def eliminar_moto(request, pk):
    moto = get_object_or_404(Moto, pk=pk)
    if request.method == 'POST':
        moto.delete()
        return redirect('lista_motos')
    return render(request, 'motosapp/eliminar_moto.html', {'moto': moto})

def login_pagina(request):
    return render(request, 'motosapp/login.html')

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(
            username = username,
            password = password
        )

        if usuario is not None:
            token, creado = Token.objects.get_or_create(
                user=usuario
            )

            return Response({
                'mensaje': 'Autenticación correcta',
                'usuario': usuario.username,
                'token': token.key
            }, status = status.HTTP_200_OK)
        return Response({
            'error': 'Usuario o contraseña incorrectos'
        }, status=status.HTTP_401_UNAUTHORIZED)

class MotosAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self):
        motos = Moto.objects.all()
        datos = []
        for moto in motos:
            datos.append({
                "id":moto.id,
                "nombre":moto.nombre,
                "marca":moto.marca,
                "anio":moto.anio,
                "cilindrada":moto.cilindrada,
                "precio":moto.precio,
                "imagen":moto.imagen
            })
        return Response(datos, status=status.HTTP_200_OK)

    def post(self, request):
        nombre = request.data.get("nombre")
        marca = request.data.get("marca")
        anio = request.data.get("anio")
        cilindrada = request.data.get("cilindrada")
        precio = request.data.get("precio")
        imagen = request.data.get("imagen")

        if not nombre or not marca or not anio or not cilindrada or not precio:
            return Response({
                "error": "Todos los campos son obligatorios"
            }, status = status.HTTP_400_BAD_REQUEST)

        moto = Moto.objects.create(
            nombre = nombre,
            marca = marca,
            anio = anio,
            cilindrada = cilindrada,
            precio = precio,
            imagen = imagen
        )

        return Response({
            "mensaje" : "Moto creada correctamente",
            "moto" : {
                "id":moto.id,
                "nombre":moto.nombre,
                "marca":moto.marca,
                "anio":moto.anio,
                "cilindrada":moto.cilindrada,
                "precio":moto.precio,
                "imagen":moto.imagen           
            }
        }, status = status.HTTP_201_CREATED)

class MotoDetalleAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, id):
        moto = get_object_or_404(Moto, id=id)

        return Response({
            "id":moto.id,
            "nombre":moto.nombre,
            "marca":moto.marca,
            "anio":moto.anio,
            "cilindrada":moto.cilindrada,
            "precio":moto.precio,
            "imagen":moto.imagen           
        }, status = status.HTTP_200_OK)

    def delete(self, id):
        moto = get_object_or_404(Moto, id=id)
        moto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        moto = get_object_or_404(Moto, id=id)

        nombre = request.data.get("nombre")
        marca = request.data.get("marca")
        anio = request.data.get("anio")
        cilindrada = request.data.get("cilindrada")
        precio = request.data.get("precio")
        imagen = request.data.get("imagen")

        if not nombre or not marca or not anio or not cilindrada or not precio:
            return Response({
                "error": "Todos los campos son obligatorios"
            }, status = status.HTTP_400_BAD_REQUEST)

        return Response({
            "id":moto.id,
            "nombre":moto.nombre,
            "marca":moto.marca,
            "anio":moto.anio,
            "cilindrada":moto.cilindrada,
            "precio":moto.precio,
            "imagen":moto.imagen
        }, status = status.HTTP_200_OK)