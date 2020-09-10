from django import forms
from .models import Civel

class CivelForm(forms.ModelForm):
    class Meta:
        model = Civel
        fields = ['nomeCivel', 'cpfCivel', 'whatsAppCivel', 'beneficiosCivel', 'tiposBeneficiosCivel', 'advogadoCivel', 'protocoloCivel', 'statusDocCivel', 'docCivel']