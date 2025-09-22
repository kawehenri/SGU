# Importa o objeto ma do módulo src, utilizado para serialização com Marshmallow
from src import ma
# Importa o modelo Servico do módulo servicos_model
from src.models import servicos_model
# Importa o módulo fields da biblioteca marshmallow para definir tipos de campos
from marshmallow import fields

#
# Define a classe ServicoSchema, herdando de SQLAlchemyAutoSchema para criar o schema de serialização do modelo Servico
class ServicoSchema(ma.SQLAlchemyAutoSchema):
    # Classe interna Meta para configurar o schema
    class Meta:
        # Define o modelo associado ao schema
        model = servicos_model.ServicoModel
        # Define os campos que serão serializados/deserializados
        fields = ("id", "descricao", "valor", "horario_duracao")

    # Campos obrigatórios
    descricao = fields.String(required=True)
    valor = fields.Float(required=True)
    horario_duracao = fields.Float(required=True)
