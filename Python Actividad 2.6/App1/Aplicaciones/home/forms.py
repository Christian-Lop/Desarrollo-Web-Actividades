from django import forms
from django.forms import fields
from .models import Estudiantes


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'