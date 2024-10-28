from models.usuario_model import Usuario
from repositories.usuario_repositories import UsuarioRepositories

class UsuarioServices:
    def __init__(self, repository = UsuarioRepositories):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if not novo_usuario:
                print("Usuário já cadastrado.")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com  sucesso.")
        except TypeError as erro:
            print("Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
