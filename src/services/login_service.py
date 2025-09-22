from src import db
from ..models.login_model import Login
from passlib.hash import pbkdf2_sha256 as sha256

def cadastrar_login(login_entity):
    login_db = Login(email=login_entity.email, senha=login_entity.senha)
    login_db.senha = sha256.hash(login_entity.senha)
    db.session.add(login_db)
    db.session.commit()
    return login_db

def listar_login():
    login_db = Login.query.all()
    return login_db

def listar_login_email(email):
    login_db = Login.query.filter_by(email=email).first()
    return login_db

def verificar_login(email, senha):
    login_db = Login.query.filter_by(email=email).first()
    if login_db and sha256.verify(senha, login_db.senha):
        return True
    return False

def excluir_login(id):
    login_db = Login.query.get(id)
    if login_db:
        db.session.delete(login_db)
        db.session.commit()
        return True
    return False
