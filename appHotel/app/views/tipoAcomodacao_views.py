from turtle import pos
from django.shortcuts import render, redirect

from..forms.tiposAcomodacao_forms import TiposAcomodacaoForm
from ..entidades import tiposAcomodacao
from ..services import tiposAcomodacao_service
from ..models import TiposAcomodacao


def listar_tiposAcomodacao(request):
    tiposAcomodacoes = tiposAcomodacao_service.listar_tiposAcomodacao
    return render(request, 'tipos/listar.html', {'tiposAcomodacoes': tiposAcomodacoes})


def cadastrar_tiposAcomodacao(request):
    if request.method == "POST":
        form_tiposAcomodacao = TiposAcomodacaoForm(request.POST or None)
        if form_tiposAcomodacao.is_valid():
            descricao = form_tiposAcomodacao.cleaned_data["descricao"]
            tiposAcomodacao_novo = tiposAcomodacao.TiposAcomodacao(descricao=descricao)
            tiposAcomodacao_service.cadastrar_tiposAcomodacao(tiposAcomodacao_novo)
            return redirect('listar_tipos')
    else:
        form_tiposAcomodacao = TiposAcomodacaoForm()
    return render(request, 'tipos/cadastrar.html', {'form_tiposAcomodacao': form_tiposAcomodacao})
    

def editar_tiposAcomodacao(request, id):
    tipo = TiposAcomodacao.objects.get(id = id)
    form_tiposAcomodacao = TiposAcomodacaoForm(request.POST or None, instance=tipo)
    if form_tiposAcomodacao.is_valid():
        form_tiposAcomodacao.save()
        return redirect('listar_tipos')
    return render(request, 'tipos/cadastrar.html', {'form_tiposAcomodacao': form_tiposAcomodacao})