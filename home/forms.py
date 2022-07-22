from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        """Se Definen para Cada Elemento los Atributos que va a Usar"""
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el Texto',
                    'class':'pingolo'
                }
            )
        }

    """Validando Variable Cantidad"""
    def clean_cantidad(self):
        """Obteniendo el Valor"""
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            """Realizar Las Validaciones"""
            raise forms.ValidationError('EL Valor Debe Ser Mayor que 10')
            
        return cantidad
