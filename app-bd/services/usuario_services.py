from models.usuario_model import Usuario
from repositories.usuario_repositories import UsuarioRepositories

class UsuarioServices:
    def __init__(self, repository = UsuarioRepositories):
        self.repository = repository

    def create_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado.")
                return 

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com  sucesso.")
        except TypeError as erro:
            print("Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        lista_usuarios = self.repository,lista_usuarios()
        print("\nListando usuários cadastrados: ")
        for usuario in lista_usuarios:
            print(f"Nome: {usuario.nome} \nEmail: {usuario.email} \nSenha: {usuario.senha}")
        #return self.repository.listar_usuarios()
    def atualizar_usuario(self):
        try: 
            print("\nAtualizando os dados de um usuário.")
            emal_usuario = input("Informe o email do usuário:")