from src import db
from ..models.servicos_model import ServicoModel
from ..entities.servico import Servico

def cadastrar_servico(servico_entity):
    servico_db = ServicoModel(
        descricao=servico_entity.descricao,
        valor=servico_entity.valor,
        horario_duracao=servico_entity.horario_duracao
    )
    db.session.add(servico_db)
    db.session.commit()
    return servico_db

def listar_servico():
    servico_db = ServicoModel.query.all()
    servico_enti = [
        Servico(s.descricao, s.valor, s.horario_duracao) for s in servico_db
    ]
    return servico_enti

def listar_servico_id(id):
    try:
        servico_encontrado = ServicoModel.query.get(id)
        if servico_encontrado:
            return Servico(servico_encontrado.descricao, servico_encontrado.valor, servico_encontrado.horario_duracao)
    except Exception as e:
        print(f'Erro ao listar servico por id {e}')
        return None

def excluir_servico(id):
    servico_db = ServicoModel.query.get(id)
    if servico_db:
        db.session.delete(servico_db)
        db.session.commit()
        return True
    return False

def editar_servico(id, servico_entity):
    servico_db = ServicoModel.query.get(id)
    if not servico_db:
        return None
    
    servico_db.descricao = servico_entity.descricao
    servico_db.valor = servico_entity.valor
    servico_db.horario_duracao = servico_entity.horario_duracao
    db.session.commit()
    
    return Servico(servico_db.descricao, servico_db.valor, servico_db.horario_duracao)
