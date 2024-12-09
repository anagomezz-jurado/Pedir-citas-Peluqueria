from django import forms
from .models import Cliente, Dependienta
class CitaForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Cliente.objects.all())
    fecha = forms.DateTimeField()
    hora = forms.TimeField()
    servicio = forms.CharField(max_length=100)
    dependienta = forms.ModelChoiceField(queryset=Dependienta.objects.all())
