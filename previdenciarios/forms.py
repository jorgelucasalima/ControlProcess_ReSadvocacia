from django import forms
from .models import Previdenciario

class PrevidenciarioForm(forms.ModelForm):
    class Meta:
        model = Previdenciario
        fields = ['nomePrev', 'cpfPrev', 'whatsAppPrev', 'beneficiosPrev', 'advogadoPrev', 'protocoloPrev', 'statusDocPrev', 'docPrev']