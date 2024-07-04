from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactoForm
from .models import Proyecto, Contacto

def index(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'myportfolio/contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'myportfolio/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'myportfolio/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'registration/vista_protegida.html')

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})