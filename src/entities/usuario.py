class Usuario:
     # construtor da classe
  
    def __init__(self, nome, email, telefone, senha):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha
    
   
# get e set para manipular os atributos
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    

    @property
    def descricao(self):
        return self._descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def horario_duracao(self):
        return self._horario_duracao

    @horario_duracao.setter
    def horario_duracao(self, horario_duracao):
        self._horario_duracao = horario_duracao
