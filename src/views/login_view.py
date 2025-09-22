from flask_restful import Resource
from marshmallow import ValidationError
from src.schemas import login_schema
from flask import request, jsonify, make_response
from src.services import login_service
from src import api

# POST-GET para login
class LoginList(Resource):
    def get(self):
        logins = login_service.listar_login()

        if not logins:
            return make_response(jsonify({'message':'Não existem logins!'}), 200)
        
        schema = login_schema.LoginSchema(many=True)
        return make_response(jsonify(schema.dump(logins)), 200)

    def post(self):
        # Verifica se o Content-Type é JSON
        if not request.is_json:
            return make_response(jsonify({'message': 'Content-Type deve ser application/json'}), 415)
        
        # Verifica se há dados JSON
        if not request.json:
            return make_response(jsonify({'message': 'Dados JSON são obrigatórios'}), 400)
        
        schema = login_schema.LoginSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        try:
            # Verificar se já existe login com este email
            if login_service.listar_login_email(dados['email']):
                return make_response(jsonify({'message': 'Email já cadastrado'}), 400)
            
            # criação do novo login no banco
            from src.entities.login import Login
            novo_login = Login(
                email=dados['email'],
                senha=dados['senha']
            )
            resultado = login_service.cadastrar_login(novo_login)
            return make_response(jsonify(schema.dump(resultado)), 201)

        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(LoginList, '/login')

class LoginResource(Resource):
    def post(self):
        """Endpoint para autenticação"""
        try:
            dados = request.json
            email = dados.get('email')
            senha = dados.get('senha')
            
            if not email or not senha:
                return make_response(jsonify({'message': 'Email e senha são obrigatórios'}), 400)
            
            if login_service.verificar_login(email, senha):
                return make_response(jsonify({'message': 'Login realizado com sucesso!'}), 200)
            else:
                return make_response(jsonify({'message': 'Email ou senha incorretos'}), 401)
                
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)
    
    def delete(self, id_login):
        login_encontrado = login_service.listar_login_id(id_login)
        if not login_encontrado:
            return make_response(jsonify({'message': 'Login não encontrado'}), 404)
        try:
            login_service.excluir_login(id_login)
            return make_response(jsonify({'message':'Login excluído com sucesso!'}), 200)
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(LoginResource, '/login/auth', '/login/<int:id_login>')
