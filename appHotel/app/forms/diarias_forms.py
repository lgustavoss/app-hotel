from django import forms
from django.forms import DateInput, TextInput

from ..models import Diarias


class DiariasForm(forms.ModelForm):
    class Meta:
        model = Diarias
        fields = '__all__'
        widgets = {
            'entrada': DateInput(
                attrs={'type': "date",
                       'oninput': 'atualizarDataDinamico(this)'}
            ),
            'saida': DateInput(
                attrs={'type': "date",
                       'oninput': 'atualizarDataDinamico(this)'}
            ),
            'qnt_diarias': TextInput(
                attrs={'type': "text",
                       'oninput': 'atualizarDataDinamico(this)'}
            ),
            'valor_diaria': TextInput(
                attrs={'type': "text",
                       'oninput': 'atualizarDataDinamico(this)',
                       'oninput': 'atualizarTotalDinamico(this)', }
            ),
            'total_diaria': TextInput(
                attrs={'type': "text", 'readonly': 'readonly',
                       }
            ),
        }
