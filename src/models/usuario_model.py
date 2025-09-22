# Importa o objeto db do módulo src, utilizado para manipulação do banco de dados com SQLAlchemy
from src import db
# Importa o algoritmo de hash pbkdf2_sha256 da biblioteca passlib e o renomeia para sha256
from passlib.hash import pbkdf2_sha256 as sha256

#
# Define a classe Usuario, que herda de db.Model, tornando-a um modelo do banco de dados
class UsuarioModel(db.Model):
    # Define o nome da tabela no banco de dados como 'tb_usuario'
    __tablename__ = "tb_usuario"

    # Coluna 'id' do tipo inteiro, chave primária, autoincrementável
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Coluna 'nome' do tipo string, não pode ser nula
    nome = db.Column(db.String(120), nullable=False)
    # Coluna 'email' do tipo string, única e não pode ser nula
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Coluna 'senha' do tipo string, não pode ser nula
    senha = db.Column(db.String(255), nullable=False)
    # Coluna 'telefone' do tipo string, não pode ser nula
    telefone = db.Column(db.String(50), nullable=False)

    # Método para gerar o hash da senha e armazenar no atributo senha
    def gen_senha(self, senha):
        self.senha = sha256.hash(senha)

    # Método para verificar se a senha fornecida confere com o hash armazenado
    def verifica_senha(self, senha):
        return sha256.verify(senha, self.senha)