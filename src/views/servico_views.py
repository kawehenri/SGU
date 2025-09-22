from flask_restful import Resource
from marshmallow import ValidationError
from src.schemas import servico_schema
from flask import request, jsonify, make_response
from src.services import servico_service
from src.entities import servico
from src import api

# POST-GET-PUT-DELETE
# Lidar com todos os serviços
class ServicoList(Resource):
    def get(self):
        servicos = servico_service.listar_servico()

        if not servicos:
            return make_response(jsonify({'message':'Não existem serviços!'}), 200)
        
        schema = servico_schema.ServicoSchema(many=True)
        return make_response(jsonify(schema.dump(servicos)), 200)

    def post(self):
        # Verifica se o Content-Type é JSON
        if not request.is_json:
            return make_response(jsonify({'message': 'Content-Type deve ser application/json'}), 415)
        
        # Verifica se há dados JSON
        if not request.json:
            return make_response(jsonify({'message': 'Dados JSON são obrigatórios'}), 400)
        
        schema = servico_schema.ServicoSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        try:
            # criação do novo serviço no banco
            novo_servico = servico.Servico(
                descricao=dados['descricao'],
                valor=dados['valor'],
                horario_duracao=dados['horario_duracao']
            )
            resultado = servico_service.cadastrar_servico(novo_servico)
            return make_response(jsonify(schema.dump(resultado)), 201)

        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(ServicoList, '/servico')

class ServicoResource(Resource):
    def get(self, id_servico):
        servico_encontrado = servico_service.listar_servico_id(id_servico)
        if not servico_encontrado:
            return make_response(jsonify({'message': 'Serviço não encontrado'}), 404)
        
        schema = servico_schema.ServicoSchema()
        return make_response(jsonify(schema.dump(servico_encontrado)), 200)
    
    def put(self, id_servico):
        schema = servico_schema.ServicoSchema()
        
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
        
        try:
            servico_atualizado = servico.Servico(
                descricao=dados['descricao'],
                valor=dados['valor'],
                horario_duracao=dados['horario_duracao']
            )
            resultado = servico_service.editar_servico(id_servico, servico_atualizado)
            
            if not resultado:
                return make_response(jsonify({'message': 'Serviço não encontrado'}), 404)
                
            return make_response(jsonify(schema.dump(resultado)), 200)
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)
    
    def delete(self, id_servico):
        servico_encontrado = servico_service.listar_servico_id(id_servico)
        if not servico_encontrado:
            return make_response(jsonify({'message': 'Serviço não encontrado'}), 404)
        try:
            servico_service.excluir_servico(id_servico)
            return make_response(jsonify({'message':'Serviço excluído com sucesso!'}), 200)
        except Exception as e:
            return make_response(jsonify({'message':str(e)}), 400)

api.add_resource(ServicoResource, '/servico/<int:id_servico>')
