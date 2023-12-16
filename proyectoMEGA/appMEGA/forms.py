from django import forms
from .models import Tipodeduccion

class TipodeduccionForm(forms.Form):
    class Meta:
        model = Tipodeduccion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_deduccion_descripcion'].choices = [('Renta (B)', 'Renta (B)'), ('Deuda pendiente(B)', 'Deuda pendiente(B)')]
