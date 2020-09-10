from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from previdenciarios.models import Previdenciario
from trabalhistas.models import Trabalhista
from civels.models import Civel

# Create your views here.


def dashboard(request):
    dashPrev = Previdenciario.objects.filter().count()
    dashTrab = Trabalhista.objects.filter().count()
    dashCivel = Civel.objects.filter().count()
    dashTotal = dashCivel + dashPrev + dashTrab
    return render(request, 'dashboard.html', {
        'dashPrev':dashPrev, 
        'dashTrab':dashTrab,
        'dashCivel':dashCivel,
        'dashTotal':dashTotal
        })