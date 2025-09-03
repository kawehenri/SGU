# Importa o objeto db do módulo src, utilizado para manipulação do banco de dados com SQLAlchemy
from src import db
#
# Define a classe Login, que herda de db.Model, tornando-a um modelo do banco de dados
class Login(db.Model):
    # Define o nome da tabela no banco de dados como 'tb_login'
    __tablename__ = "tb_login"

    # Coluna 'id' do tipo inteiro, chave primária, autoincrementável
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Coluna 'email' do tipo string, não pode ser nula
    email = db.Column(db.String(120), nullable=False)
    # Coluna 'senha' do tipo string, não pode ser nula
    senha = db.Column(db.String(200), nullable=False)

    # Método construtor da classe Login, inicializa os atributos email e senha
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha