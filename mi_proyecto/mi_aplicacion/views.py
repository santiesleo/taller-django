from django.shortcuts import render, redirect
from .models import Articulo
from .forms import ArticuloForm
# Create your views here.

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'mi_aplicacion/lista_articulos.html', {'articulos': articulos})

def nuevo_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'mi_aplicacion/nuevo_articulo.html', {'form': 
form})