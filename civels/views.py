from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Civel
from .forms import CivelForm

# Create your views here.

def list_civels(request):
    civels_list = Civel.objects.all()
    paginator = Paginator(civels_list, 10)
    page = request.GET.get('page')
    civels = paginator.get_page(page)
    '''
        realizando a busca e filtrando na tabela
    '''
    busca = request.GET.get('search')
    if busca:
        civels =Civel.objects.filter(cpfCivel__icontains = busca)
    return render(request, 'civel.html', {'civels':civels})

def create_civel(request):
    form = CivelForm(request.POST, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_civels')
        
    return render(request, 'civels-form.html', {'form':form})

def update_civel(request,id):
    civel = Civel.objects.get(id=id)
    form = CivelForm(request.POST or None, instance=civel)

    if form.is_valid():
        form.save()
        return redirect('list_civels')

    return render(request, 'civels-form.html', {'form':form, 'civel':civel})

def delete_civel(request, id):
    civel = Civel.objects.get(id=id)

    if request.method == 'POST':
        civel.delete()
        return redirect('list_civels')

    return render(request, 'civel-delete-confirm.html', {'civel':civel})

