from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Trabalhista
from .forms import TrabalhistaForm

# Create your views here.

def list_trabalhistas(request):
    trabalhistas_list = Trabalhista.objects.all()
    paginator = Paginator(trabalhistas_list, 10)
    page = request.GET.get('page')
    trabalhistas = paginator.get_page(page)
    '''
        realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        trabalhistas = Trabalhista.objects.filter(cpfTrab__icontains = busca)
    return render(request, 'trabalhista.html', {'trabalhistas':trabalhistas})

def create_trabalhista(request):
    form = TrabalhistaForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_trabalhistas')
        
    return render(request, 'trabalhistas-form.html', {'form':form})

def update_trabalhista(request,id):
    trabalhista = Trabalhista.objects.get(id=id)
    form = TrabalhistaForm(request.POST or None, instance=trabalhista)

    if form.is_valid():
        form.save()
        return redirect('list_trabalhistas')

    return render(request, 'trabalhistas-form.html', {'form':form, 'trabalhista':trabalhista})

def delete_trabalhista(request, id):
    trabalhista = Trabalhista.objects.get(id=id)

    if request.method == 'POST':
        trabalhista.delete()
        return redirect('list_trabalhistas')

    return render(request, 'trabalhista-delete-confirm.html', {'trabalhista':trabalhista})