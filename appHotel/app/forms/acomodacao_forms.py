from tabnanny import check
from django import forms
from django.forms import CheckboxInput
from ..models import Acomodacao


class AcomodacaoForm(forms.ModelForm):
    class Meta:
        model = Acomodacao
        fields = '__all__'
        ordering = ('order', 'unidade')
