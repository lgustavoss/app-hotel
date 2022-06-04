from ..models import TiposAcomodacao


def cadastrar_tiposAcomodacao(tiposAcomodacao):
    TiposAcomodacao.objects.create(
        descricao=tiposAcomodacao.descricao)


def listar_tiposAcomodacao():
    return TiposAcomodacao.objects.all()


def listar_tiposAcomodacao_id(id):
    return TiposAcomodacao.objects.get(id=id)


def editar_tiposAcomodacao(tiposAcomodacao, tipoAcomodacao_novo):
    tiposAcomodacao.descricao = tipoAcomodacao_novo.descricao
    tiposAcomodacao.up(force_update=True)
