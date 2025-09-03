# Importa a classe Resource do flask_restful para criar recursos REST
from flask_restful import Resource
# Importa ValidationError do marshmallow para tratar erros de validação
from marshmallow import ValidationError
# Importa o módulo usuario_services para acessar funções de serviço de usuário
from src.services import usuario_services
# Importa request, jsonify e make_response do flask para manipular requisições e respostas HTTP
from flask import request, jsonify, make_response
# Importa novamente usuario_services (pode ser removido se duplicado)
from src.services import usuario_services
# Importa o objeto api do módulo src para registrar recursos na API
from src import api
from src.models.usuario_model import Usuario

# POST - GET - PUT - DELETE
# Classe para lidar com os endpoints relacionados a usuários
class UsuarioList(Resource):
    # Método GET para listar usuários
    def get(self):
        # Busca todos os usuários cadastrados
        usuarios = usuario_services.listar_usuarios()

        # Se não houver usuários, retorna mensagem informando
        if not usuarios:
            return make_response(jsonify({"message": "Nenhum usuário encontrado."}))
        
        # Cria um schema para serializar múltiplos usuários
        schema = usuario_services.usuario_schema.UsuarioSchema(many=True)

        # Retorna a lista de usuários serializada com status 200
        return make_response(jsonify(schema.dump(usuarios)), 200)

    # Método POST para cadastrar um novo usuário
    def post(self):
        schema = usuario_services.usuario_schema.UsuarioSchema()

        try:
            dados = schema.load(request.json) # load = desserializa o json
        except ValidationError as e:
            return make_response(jsonify(e.messages), 400)

        if usuario_services.listar_usuario_email(dados["email"]):
            return make_response(jsonify({"error": "Email já cadastrado."}), 400)
        
        try:
            # criação de novo usuario
            novo_usuario = Usuario(
                nome=dados["nome"],
                email=dados["email"],
                senha=dados["senha"],
                telefone=dados["telefone"]
            )

            # Adiciona o novo usuário ao banco de dados
            resultado = usuario_services.cadastrar_usuario(novo_usuario)

            return make_response(jsonify(schema.dump(resultado)), 201) # dump = serializa o objeto
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)  # make_response = manda o valor em json

# Adiciona o recurso UsuarioList à rota '/usuarios' na API
api.add_resource(UsuarioList, '/usuarios')