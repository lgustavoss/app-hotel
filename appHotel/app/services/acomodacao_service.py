from ..models import Acomodacao


def cadastrar_acomodacao(acomodacao):
    Acomodacao.objects.create(
        unidade=acomodacao.unidade, tipo=acomodacao.tipo, andar=acomodacao.andar,
        ramal=acomodacao.ramal, capacidade=acomodacao.capacidade,
        valor=acomodacao.valor, status=acomodacao.status, situacao=acomodacao.situacao)


def listar_acomodacoes():
    return Acomodacao.objects.all()


def listar_acomodacao_id(id):
    return Acomodacao.objects.get(id=id)


def editar_acomodacao(acomodacao, acomodacao_novo):
    acomodacao.unidade = acomodacao_novo.unidade
    acomodacao.tipo = acomodacao_novo.tipo
    acomodacao.andar = acomodacao_novo.andar
    acomodacao.ramal = acomodacao_novo.ramal
    acomodacao.capacidade = acomodacao_novo.capacidade
    acomodacao.valor = acomodacao_novo.valor
    acomodacao.status = acomodacao_novo.status
    acomodacao.situacao = acomodacao_novo.situacao
    acomodacao.save(force_update=True)
