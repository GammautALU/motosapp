from datetime import date
from django import forms
from .models import Moto


class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['nombre', 'marca', 'anio', 'cilindrada', 'precio']

    def clean_anio(self):
        anio = self.cleaned_data['anio']
        if anio < 1900 or anio > date.today().year + 1:
            raise forms.ValidationError('Ingresa un año válido (entre 1900 y el próximo año).')
        return anio

    def clean_cilindrada(self):
        cilindrada = self.cleaned_data['cilindrada']
        if cilindrada <= 0:
            raise forms.ValidationError('La cilindrada debe ser mayor que cero.')
        return cilindrada

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio


class MotoEditarForm(MotoForm):
    """Formulario independiente para editar (hereda las validaciones)."""
    pass