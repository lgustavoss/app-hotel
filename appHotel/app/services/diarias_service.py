from ..models import Diarias


def cadastrar_diarias(diarias):
    Diarias.objects.create(
        cliente=diarias.cliente,
        unidade=diarias.unidade,
        hospedes=diarias.hospedes,
        entrada=diarias.entrada,
        saida=diarias.saida,
        qnt_diarias=diarias.qnt_diarias,
        valor_diaria=diarias.valor_diaria,
        total_diaria=diarias.total_diaria,
        adiantamento=diarias.adiantamento, 
        observacao=diarias.observacao)


def listar_diarias():
    return Diarias.objects.all()


def listar_diarias_id():
    return Diarias.objects.get(id=id)


def editar_diarias(diarias, diarias_novo):
    diarias.cliente = diarias_novo.cliente
    diarias.unidade = diarias_novo.unidade
    diarias.hospedes = diarias_novo.hospedes
    diarias.entrada = diarias_novo.entrada
    diarias.saida = diarias_novo.saida
    diarias.qnt_diarias = diarias_novo.qnt_diarias
    diarias.valor_diaria = diarias_novo.valor_diaria
    diarias.total_diaria = diarias_novo.total_diaria
    diarias.adiantamento = diarias_novo.adiantamento
    diarias.observacao = diarias_novo.observacao
    diarias.save(force_update=True)
    