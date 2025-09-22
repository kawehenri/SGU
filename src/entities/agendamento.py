from datetime import datetime

class Agendamento:
    def __init__(self, dt_atendimento, id_user, id_profissional, id_servico, valor_total=0.00):
        self.dt_atendimento = dt_atendimento
        self.id_user = id_user
        self.id_profissional = id_profissional
        self.id_servico = id_servico
        self.valor_total = valor_total
        self.dt_agendamento = datetime.utcnow()
        self.status = 'agendado'
    
    def __repr__(self):
        return f"Agendamento(id_user={self.id_user}, id_profissional={self.id_profissional}, dt_atendimento='{self.dt_atendimento}')"
