from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Previdenciario
from .forms import PrevidenciarioForm

# Create your views here.

def list_previdenciarios(request):
    previdenciarios_list = Previdenciario.objects.all()
    paginator = Paginator(previdenciarios_list, 10)
    page = request.GET.get('page')
    previdenciarios = paginator.get_page(page)
    '''
        realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        previdenciarios = Previdenciario.objects.filter(cpfPrev__icontains = busca)
    return render(request, 'previdenciario.html', {'previdenciarios':previdenciarios})

def create_previdenciario(request):
    form = PrevidenciarioForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_previdenciarios')
        
    return render(request, 'previdenciarios-form.html', {'form':form})

def update_previdenciario(request,id):
    previdenciario = Previdenciario.objects.get(id=id)
    form = PrevidenciarioForm(request.POST or None, instance=previdenciario)

    if form.is_valid():
        form.save()
        return redirect('list_previdenciarios')

    return render(request, 'previdenciarios-form.html', {'form':form, 'previdenciario':previdenciario})

def delete_previdenciario(request, id):
    previdenciario = Previdenciario.objects.get(id=id)

    if request.method == 'POST':
        previdenciario.delete()
        return redirect('list_previdenciarios')

    return render(request, 'previdenciario-delete-confirm.html', {'previdenciario':previdenciario})

