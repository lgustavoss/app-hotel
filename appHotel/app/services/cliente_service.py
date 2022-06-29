from ..models import Cliente


def cadastrar_cliente(cliente):
    Cliente.objects.create(
        nome=cliente.nome, cpf_cnpj=cliente.cpf_cnpj, telefone=cliente.telefone)


def listar_clientes():
    return Cliente.objects.order_by("nome").all()


def listar_cliente_id(id):
    return Cliente.objects.get(id=id)


def editar_cliente(cliente, cliente_novo):
    cliente.nome = cliente_novo.nome
    cliente.cpf_cnpj = cliente_novo.cpf_cnpj
    cliente.telefone = cliente_novo.telefone
    cliente.save(force_update=True)
