from django.shortcuts import redirect
from django.shortcuts import render
from portal.forms import AutorForm
from portal.models import Autor, Editora, Formato, Livro


# Create your views here.
def home(requests):
    return render(requests, 'portal/home.html')

def dashboard(requests):
    return render(requests, 'portal/dashboard.html')

#LISTA DE AUTORES
def autor(requests):
    autores = Autor.objects.all()
    context = {
        'autores': autores 
    }
    return render(requests, 'portal/autor.html', context)

#ADICIONAR AUTOR
def autor_add(requests):
    form = AutorForm(requests.POST or None)

    if requests.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form
    }
    return render(requests, 'portal/autor_add.html', context)

#EDITAR UM AUTOR
def autor_edit(requests, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)

    form = AutorForm(requests.POST or None, instance=autor)

    if requests.POST:
        if form.is_valid():
            form.save()
            return redirect('autor')

    context = {
        'form': form,
    }
    return render(requests, 'portal/autor_edit.html', context)

#APAGAR UM AUTOR
def autor_delete(requests, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor_delete()

    return redirect('autor')

def editora(requests):
    return render(requests, 'portal/editora.html')

def formato(requests):
    return render(requests, 'portal/formato.html')

def livro(requests):
    return render(requests, 'portal/livro.html')



