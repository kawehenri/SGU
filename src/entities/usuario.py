class Usuario:
     # construtor da classe
  
    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
    
    def __repr__(self):
        return f"Usuario(nome='{self.nome}', email='{self.email}')"
