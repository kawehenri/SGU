# Importa a classe Flask e o objeto request do Flask
from flask import Flask , request
# Importa a extensão SQLAlchemy para integração ORM
from flask_sqlalchemy import SQLAlchemy
# Importa a extensão Migrate para migrações do banco de dados
from flask_migrate import Migrate
# Importa a extensão Marshmallow para serialização
from flask_marshmallow import Marshmallow
# Importa a extensão CORS para permitir requisições de diferentes origens
from flask_cors import CORS 
# Importa a classe Api do flask_restful para criar APIs REST
from flask_restful import Api

# Cria a aplicação Flask
app = Flask(__name__)

# Importa as configurações do arquivo connection.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from connection import SQLALCHEMY_DATABASE_URI, SECRET_KEY

# Configura a aplicação Flask
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializa o SQLAlchemy com a aplicação
db = SQLAlchemy(app)
# Inicializa o Migrate para controle de migrações
migrate = Migrate(app, db)
# Inicializa o Marshmallow para serialização
ma = Marshmallow(app)
# Inicializa a API RESTful
api = Api(app)
# Habilita CORS na aplicação
CORS(app)

# Função executada antes de cada requisição
@app.before_request
def before_request():
    # Se o endpoint for 'index', cria todas as tabelas do banco de dados
    if request.endpoint == 'index':
        db.create_all()

# Importa todos os modelos do pacote models
from .models import *

# Função para criar todas as tabelas
def create_all_tables():
    """Cria todas as tabelas do banco de dados"""
    with app.app_context():
        try:
            db.create_all()
            print("✅ Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao criar tabelas: {e}")

# Criar tabelas automaticamente quando o módulo é importado
create_all_tables()

# TODO: Importar as views para API encontrar as rotas
from .views import *