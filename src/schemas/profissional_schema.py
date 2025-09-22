# Importa o objeto ma do módulo src, utilizado para serialização com Marshmallow
from src import ma
# Importa o modelo Profissional do módulo profissional_model
from src.models import profissional_model
# Importa o módulo fields da biblioteca marshmallow para definir tipos de campos
from marshmallow import fields

#
# Define a classe ProfissionalSchema, herdando de SQLAlchemyAutoSchema para criar o schema de serialização do modelo Profissional
class ProfissionalSchema(ma.SQLAlchemyAutoSchema):
    # Classe interna Meta para configurar o schema
    class Meta:
        # Define o modelo associado ao schema
        model = profissional_model.ProfissionalModel
        # Define os campos que serão serializados/deserializados
        fields = ("id", "nome")

    # Campo 'nome' do tipo string, obrigatório
    nome = fields.String(required=True)
