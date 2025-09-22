from src import db
from ..models.profissional_model import ProfissionalModel
from ..entities.profissional import Profissional

def cadastrar_profissional(profissional_entity):
    profissional_db = ProfissionalModel(nome=profissional_entity.nome)
    db.session.add(profissional_db)
    db.session.commit()
    return profissional_db

def listar_profissional():
    profissional_db = ProfissionalModel.query.all()
    profissional_enti = [
        Profissional(p.nome) for p in profissional_db
    ]
    return profissional_enti

def listar_profissional_id(id):
    try:
        profissional_encontrado = ProfissionalModel.query.get(id)
        if profissional_encontrado:
            return Profissional(profissional_encontrado.nome)
    except Exception as e:
        print(f'Erro ao listar profissional por id {e}')
        return None

def excluir_profissional(id):
    profissional_db = ProfissionalModel.query.get(id)
    if profissional_db:
        db.session.delete(profissional_db)
        db.session.commit()
        return True
    return False

def editar_profissional(id, profissional_entity):
    profissional_db = ProfissionalModel.query.get(id)
    if not profissional_db:
        return None
    
    profissional_db.nome = profissional_entity.nome
    db.session.commit()
    
    return Profissional(nome=profissional_db.nome)
