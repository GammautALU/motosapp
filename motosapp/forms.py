from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['nombre', 'marca', 'anio', 'cilindrada', 'precio']