from turtle import pos
from django.shortcuts import render, redirect, get_object_or_404

from..forms.tiposAcomodacao_forms import TiposAcomodacaoForm
from ..entidades import tiposAcomodacao
from ..services import tiposAcomodacao_service


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
    tiposAcomodacao_editar = get_object_or_404(tiposAcomodacao, id=id)
    form_tiposAcomodacao = TiposAcomodacaoForm(instance=tiposAcomodacao_editar)

    if(request.method == 'POST'):
        form_tiposAcomodacao = TiposAcomodacaoForm(request.POST, instance=tiposAcomodacao)

        if (form_tiposAcomodacao.is_valid()):
            tiposAcomodacao = form_tiposAcomodacao.save(commit=False)
            tiposAcomodacao.descricao = form_tiposAcomodacao.cleaned_data['descricao']

            form_tiposAcomodacao.save()

            return redirect('listar_tipos')
        else:
            return render(request, 'tipos/cadastrar.html', {'form_tiposAcomodacao': form_tiposAcomodacao, 'tiposAcomodacao': tiposAcomodacao})
    elif(request.method == 'GET'):
        return render(request, 'tipos/cadastrar.html', {'form_tiposAcomodacao': form_tiposAcomodacao, 'tiposAcomodacao': tiposAcomodacao})