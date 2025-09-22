# Importa o objeto ma do módulo src, utilizado para serialização com Marshmallow
from src import ma
# Importa o modelo Usuario do módulo usuario_model
from src.models import usuario_model
# Importa o módulo fields da biblioteca marshmallow para definir tipos de campos
from marshmallow import fields

#
# Define a classe UsuarioSchema, herdando de SQLAlchemyAutoSchema para criar o schema de serialização do modelo Usuario
class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    # Classe interna Meta para configurar o schema
    class Meta:
        # Define o modelo associado ao schema
        model = usuario_model.UsuarioModel
        # Define os campos que serão serializados/deserializados
        fields = ("id", "nome", "email", "senha", "telefone")

    # Campo 'nome' do tipo string, obrigatório
    nome = fields.String(required=True)
    # Campo 'email' do tipo string, obrigatório
    email = fields.String(required=True)
    # Campo 'senha' do tipo string, obrigatório
    senha = fields.String(required=True)
    # Campo 'telefone' do tipo string, obrigatório
    telefone = fields.String(required=True)