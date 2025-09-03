# Importa o módulo usuario_model do diretório models (um nível acima)
from ..models import usuario_model
# Importa o objeto db do módulo src, utilizado para manipulação do banco de dados
from src import db
# Importa o módulo usuario_schema do diretório schemas (um nível acima)
from ..schemas import usuario_schema


# Função para cadastrar um novo usuário no banco de dados
def cadastrar_usuario(usuario):
    # Cria uma instância de Usuario com nome e email recebidos
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email)
    # Gera o hash da senha e armazena no objeto usuario_db
    usuario_db.gen_senha(usuario.senha)
    # Adiciona o novo usuário à sessão do banco de dados
    db.session.add(usuario_db)
    # Salva (commita) as alterações no banco de dados
    db.session.commit()
    # Retorna o objeto usuario_db criado
    return usuario_db
    
# Função para listar todos os usuários cadastrados
def listar_usuarios():
    # Busca todos os usuários no banco de dados
    usuarios = usuario_model.Usuario.query.all()
    # Cria um schema para serializar múltiplos usuários
    schema = usuario_schema.UsuarioSchema(many=True)
    # Retorna todos os usuários encontrados
    return usuario_model.Usuario.query.all() 

def listar_usuario_id(id):
    ...

def excluir_usuario():
    ...

def editar_usuario():
    ...

def listar_usuario_email(email):
    # Busca um usuário pelo email no banco de dados
    return usuario_model.Usuario.query.filter_by(email=email).first()
