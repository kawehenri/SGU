from datetime import datetime
from src import db

class AgendamentoModel(db.Model):

    __tablename__ = 'tb_agendamentos'
    
    # Campos principais
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dt_agendamento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dt_atendimento = db.Column(db.DateTime, nullable=False)
    
    # Chaves estrangeiras
    id_user = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('tb_profissional.id'), nullable=False)
    id_servico = db.Column(db.Integer, db.ForeignKey('tb_servico.id'), nullable=False)
    
    # Campos adicionais
    status = db.Column(db.String(20), nullable=False, default='agendado')
    valor_total = db.Column(db.Float, nullable=False, default=0.00)
    taxa_cancelamento = db.Column(db.Float, nullable=True, default=0.00)
    
    # Relacionamentos
    usuario = db.relationship("UsuarioModel", backref="agendamentos")
    profissional = db.relationship("ProfissionalModel", backref="agendamentos")
    servico = db.relationship("ServicoModel", backref="agendamentos")
    
    def __init__(self, dt_atendimento, id_user, id_profissional, id_servico, 
                 valor_total=0.00):
        self.dt_atendimento = dt_atendimento
        self.id_user = id_user
        self.id_profissional = id_profissional
        self.id_servico = id_servico
        self.valor_total = valor_total
        self.dt_agendamento = datetime.utcnow()
        self.status = 'agendado'