# Importa todos os modelos para que sejam registrados no SQLAlchemy
# IMPORTANTE: Importar primeiro as tabelas base, depois as que têm chaves estrangeiras

# Tabelas base (sem chaves estrangeiras)
from .usuario_model import UsuarioModel
from .profissional_model import ProfissionalModel
from .servicos_model import ServicoModel
from .login_model import Login

# Tabelas com chaves estrangeiras (importar por último)
from .agendamento_model import AgendamentoModel

# Lista de todos os modelos para facilitar importações
__all__ = ['UsuarioModel', 'ProfissionalModel', 'ServicoModel', 'Login', 'AgendamentoModel']