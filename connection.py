# Importa a função create_engine do SQLAlchemy para criar a conexão com o banco de dados
from sqlalchemy import create_engine
# Importa declarative_base do SQLAlchemy para criar classes base para modelos ORM
from sqlalchemy.orm import declarative_base
# Importa load_dotenv para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
# Importa o módulo os para acessar variáveis de ambiente
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do banco de dados SQLite
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db" 
# Obtém a chave secreta das variáveis de ambiente
SECRET_KEY = os.getenv("SECRET_KEY")

# Teste de conexão com o banco de dados
try:
    # Cria o engine de conexão com o banco de dados
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    # Estabelece a conexão
    connection = engine.connect()
    # Se a conexão for bem-sucedida, imprime mensagem
    print("Conexão bem-sucedida!")
except Exception as e:
    # Em caso de erro, imprime mensagem de erro
    print(f"Erro ao conectar ao banco de dados: {e}")

# Cria a classe base para os modelos ORM
Base = declarative_base()