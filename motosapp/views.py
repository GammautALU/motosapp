from django.shortcuts import render, redirect, get_object_or_404
from .models import Moto
from .forms import MotoForm

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