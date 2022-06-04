from django import forms
from ..models import Acomodacao


class AcomodacaoForm(forms.ModelForm):
    situacao = forms.BooleanFieldattrs={'class': 'custom-control-input'}

    class Meta:
        model = Acomodacao
        fields = '__all__'
