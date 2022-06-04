from django.shortcuts import render, redirect

from ..forms.acomodacao_forms import AcomodacaoForm
from ..entidades import acomodacao
from ..services import acomodacao_service


def listar_acomodacoes(request):
    acomodacoes = acomodacao_service.listar_acomodacoes
    return render(request, 'acomodacao/listar.html', {'acomodacoes': acomodacoes})


def cadastrar_acomodacoes(request):
    if request.method == "POST":
        form_acomodacao = AcomodacaoForm(request.POST)
        if form_acomodacao.is_valid():
            unidade = form_acomodacao.cleaned_data["unidade"]
            tipo = form_acomodacao.cleaned_data["tipo"]
            andar = form_acomodacao.cleaned_data["andar"]
            ramal = form_acomodacao.cleaned_data["ramal"]
            capacidade = form_acomodacao.cleaned_data["capacidade"]
            valor = form_acomodacao.cleaned_data["valor"]
            status = form_acomodacao.cleaned_data["status"]
            situacao = form_acomodacao.cleaned_data["situacao"]
            acomodacao_novo = acomodacao.Acomodacao(
                unidade=unidade, tipo=tipo, andar=andar, ramal=ramal,
                capacidade=capacidade, valor=valor, status=status, situacao=situacao
            )
            acomodacao_service.cadastrar_acomodacao(acomodacao_novo)
            return redirect('acomodacao_listar')
    else:
        form_acomodacao = AcomodacaoForm()
    return render(request, 'acomodacao/cadastrar.html', {'form_acomodacao': form_acomodacao})


def editar_acomodacao(request, id):
    acomodacao_editar = acomodacao_service.listar_acomodacao_id(id)
    form_acomodacao = AcomodacaoForm(
        request.POST or None, instance=acomodacao_editar)
    if form_acomodacao.is_valid():
        unidade = form_acomodacao.cleaned_data["unidade"]
        tipo = form_acomodacao.cleaned_data["tipo"]
        andar = form_acomodacao.cleaned_data["andar"]
        ramal = form_acomodacao.cleaned_data["ramal"]
        capacidade = form_acomodacao.cleaned_data["capacidade"]
        valor = form_acomodacao.cleaned_data["valor"]
        status = form_acomodacao.cleaned_data["status"]
        acomodacao_novo = acomodacao.Acomodacao(
            unidade=unidade, tipo=tipo, andar=andar, ramal=ramal,
            capacidade=capacidade, valor=valor, status=status
        )
        acomodacao_service.cadastrar_acomodacao(acomodacao_novo)
        return redirect('acomodacao_listar')
    return render(request, 'acomodacao/cadastrar.html', {'form_acomodacao': form_acomodacao})
