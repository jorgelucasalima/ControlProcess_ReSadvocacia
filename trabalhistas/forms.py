from django import forms
from .models import Trabalhista


class TrabalhistaForm(forms.ModelForm):
    class Meta:
        model = Trabalhista
        fields = [
            'nomeTrab', 
            'cpfTrab', 
            'whatsAppTrab', 
            'beneficiosTrab', 
            'advogadoTrab', 
            'protocoloTrab', 
            'statusDocTrab',
            'docTrab'

        ]
    