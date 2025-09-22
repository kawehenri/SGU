from flask_restful import Resource
from marshmallow import ValidationError
from src.schemas import profissional_schema
from flask import request, jsonify, make_response
from src.services import profissional_service
from src.entities import profissional
from src import api

# POST-GET-PUT-DELETE
# Lidar com todos os profissionais
class ProfissionalList(Resource):
    def get(self):
        profissionais = profissional_service.listar_profissional()

        if not profissionais:
            return make_response(jsonify({'message':'Não existem profissionais!'}), 200)
        
        schema = profissional_schema.ProfissionalSchema(many=True)
        return make_response(jsonify(schema.dump(profissionais)), 200)

    def post(self):
        # Verifica se o Content-Type é JSON
        if not request.is_json:
            return make_response(jsonify({'message': 'Content-Type deve ser application/json'}), 415)
        
        # Verifica se há dados JSON
        if not request.json:
            return make_response(jsonify({'message': 'Dados JSON são obrigatórios'}), 400)
        
        schema = profissional_schema.ProfissionalSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        try:
            # criação do novo profissional no banco
            novo_profissional = profissional.Profissional(
                nome=dados['nome']
            )
            resultado = profissional_service.cadastrar_profissional(novo_profissional)
            return make_response(jsonify(schema.dump(resultado)), 201)

        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(ProfissionalList, '/profissional')

class ProfissionalResource(Resource):
    def get(self, id_profissional):
        profissional_encontrado = profissional_service.listar_profissional_id(id_profissional)
        if not profissional_encontrado:
            return make_response(jsonify({'message': 'Profissional não encontrado'}), 404)
        
        schema = profissional_schema.ProfissionalSchema()
        return make_response(jsonify(schema.dump(profissional_encontrado)), 200)
    
    def put(self, id_profissional):
        schema = profissional_schema.ProfissionalSchema()
        
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        try:
            profissional_atualizado = profissional.Profissional(
                nome=dados['nome']
            )
            resultado = profissional_service.editar_profissional(id_profissional, profissional_atualizado)
            
            if not resultado:
                return make_response(jsonify({'message': 'Profissional não encontrado'}), 404)
                
            return make_response(jsonify(schema.dump(resultado)), 200)
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)
    
    def delete(self, id_profissional):
        profissional_encontrado = profissional_service.listar_profissional_id(id_profissional)
        if not profissional_encontrado:
            return make_response(jsonify({'message': 'Profissional não encontrado'}), 404)
        try:
            profissional_service.excluir_profissional(id_profissional)
            return make_response(jsonify({'message':'Profissional excluído com sucesso!'}), 200)
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(ProfissionalResource, '/profissional/<int:id_profissional>')
