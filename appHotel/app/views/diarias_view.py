from django.shortcuts import render, redirect

from ..forms.diarias_forms import DiariasForm
from ..entidades import diarias
from ..services import diarias_service
from ..models import Diarias


def listar_diarias(request):
    diarias = diarias_service.listar_diarias
    return render(request, 'diarias/listar.html', {'diarias': diarias})


def cadastrar_diarias(request):
    if request.method == 'POST':
        form_diarias = DiariasForm(request.POST)
        if form_diarias.is_valid():
            cliente = form_diarias.cleaned_data["cliente"]
            unidade = form_diarias.cleaned_data["unidade"]
            hospedes = form_diarias.cleaned_data["hospedes"]
            entrada = form_diarias.cleaned_data["entrada"]
            saida = form_diarias.cleaned_data["saida"]
            qnt_diarias = form_diarias.cleaned_data["qnt_diarias"]
            valor_diaria = form_diarias.cleaned_data["valor_diaria"]
            total_diaria = form_diarias.cleaned_data["total_diaria"]
            adiantamento = form_diarias.cleaned_data["adiantamento"]
            observacao = form_diarias.cleaned_data["observacao"]
            diaria_novo = diarias.Diarias(
                cliente=cliente, unidade=unidade, hospedes=hospedes, entrada=entrada, saida=saida,
                qnt_diarias=qnt_diarias, valor_diaria=valor_diaria, total_diaria=total_diaria,
                adiantamento=adiantamento, observacao=observacao)
            diarias_service.cadastrar_diarias(diaria_novo)
            return redirect('listar_diarias')
    else:
        form_diarias = DiariasForm
    return render(request, 'diarias/cadastrar.html', {'form_diarias': form_diarias})


def editar_diarias(request, id):
    diarias_editar = Diarias.objects.get(id=id)
    form_diarias = DiariasForm(request.POST or None, instance=diarias_editar)
    if form_diarias.is_valid():
        form_diarias.save()
        return redirect('listar_diarias')
    return render(request, 'diarias/cadastrar.html', {'form_diarias': form_diarias})
