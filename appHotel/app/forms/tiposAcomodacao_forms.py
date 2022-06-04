from django import forms
from ..models import TiposAcomodacao


class TiposAcomodacaoForm(forms.ModelForm):
    class Meta:
        model = TiposAcomodacao
        fields = '__all__'
