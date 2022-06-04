from django.shortcuts import render, redirect

from ..forms.cliente_forms import ClienteForm
from ..entidades import cliente
from ..services import cliente_service


def listar_clientes(request):
    clientes = cliente_service.listar_clientes
    return render(request, 'cliente/listar.html', {'clientes': clientes})


def cadastrar_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST or None)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            cpf_cnpj = form_cliente.cleaned_data["cpf_cnpj"]
            telefone = form_cliente.cleaned_data["telefone"]
            cliente_novo = cliente.Cliente(
                nome=nome, cpf_cnpj=cpf_cnpj, telefone=telefone)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
    else:
        form_cliente = ClienteForm()
    return render(request, 'cliente/cadastrar.html', {'form_cliente': form_cliente})


def editar_cliente(request, id):
    cliente_editar = cliente_service.listar_cliente_id(id)
    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data["nome"]
        cpf_cnpj = form_cliente.cleaned_data["cpf_cnpj"]
        telefone = form_cliente.cleaned_data["telefone"]
        cliente_novo = cliente.Cliente(
            nome=nome, cpf_cnpj=cpf_cnpj, telefone=telefone)
        cliente_service.editar_cliente(cliente_editar, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'cliente/cadastrar.html', {'form_cliente': form_cliente})