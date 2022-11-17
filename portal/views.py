from django.shortcuts import render
from portal.forms import AutorForm
from portal.models import Autor, Editora, Formato, Livro


# Create your views here.
def home(requests):
    return render(requests, 'portal/home.html')

def dashboard(requests):
    return render(requests, 'portal/dashboard.html')

def autor(requests):
    autores = Autor.objects.all()
    context = {
        'autores': autores 
    }
    return render(requests, 'portal/autor.html', context)

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

def editora(requests):
    return render(requests, 'portal/editora.html')

def formato(requests):
    return render(requests, 'portal/formato.html')

def livro(requests):
    return render(requests, 'portal/livro.html')



