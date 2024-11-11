from app.models.usuario_model import Usuario
from app.repositories.usuario_repositories import UsuarioRepositories
from app.config.database import Session

session = Session()

class UsuarioServices:
    def __init__(self, repository = UsuarioRepositories):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
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
            return self.repository.listar_usuarios()
    
    def atualizar_usuario(self):
        try: 
            print("\nAtualizando os dados de um usuário.")

            email = input("Informe o email do usuário:")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                cadastrado.nome = input("\nDigite um novo nome")
                cadastrado.email = input("\nDigite um novo email")
                cadastrado.senha = input("\nDigite um novo senha")
                self.repository.atualizar_usuario(cadastrado)
                print("Cadastrado com sucesso.")
            else:
                print("\nDados de usuário não encontrado.")
                return
        except TypeError as erro:
            print("Erro ao atualizar o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")
        
    def excluir_usuario(self):
        try:
            print("\nExcluindo dados do usuário.")

            email = input("Informe o email do usuário que será excluido:")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if cadastrado:
                self.repository.excluir_usuario(cadastrado)
                print("\nUsuário excluido.")
            else:
                print("\nUsuário não encontrado.")
                return
            
        except TypeError as erro:
            print("Erro ao excluir o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")
    
    def consultar_usuario(self):
        try:
            email = input("\nInforme o email do usuário que deseja consultar: ")
            cadastrado = self.repository.pesquisar_usuario_por_email(email)

            #usuario = session.query(Usuario).filter_by(email=email).first()

            if cadastrado:
                print(f"{cadastrado.id} - {cadastrado.nome} - {cadastrado.email} - {cadastrado.senha}")
            else:
                print("Usuário não encontrado. ")
            return
        
        except TypeError as erro:
            print("Erro ao procurar o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")

"""
def create_usuario():
    # Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = str(input("Digite seu nome: "))
    email = str(input("Digite seu email: "))
    senha = str(input("Digite sua senha: "))

    usuario = Usuario(nome=nome, email=email, senha=senha)
    session.add(usuario)
    session.commit()
    return create_usuario


def read_usuario():
    lista_usuarios = session.query(Usuario).all()

    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

    return read_usuario


def update_usuario():
    email_usuario = input("Digite o email do usuario que será atualizado: ")

    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario:
        usuario.nome = input("Digite seu nome: ")
        usuario.email = input("Digite seu e-mail: ")
        usuario.senha = input("Digite sua senha: ")

        session.commit()
    else:
        print("Usuário não encontrado. ")
    return update_usuario


def delete_usuario():
    email_usuario = input("Digite o email do usuario que será excluído: ")

    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario:
        session.delete(usuario)
        session.commit()
        print(f"Usuário {usuario.nome} excluído com sucesso! ")
    else:
        print("Usuário não encontrado. ")
    return delete_usuario


def consultar_usuario():
    email_usuario = input("Digite o email do usuário: ")

    usuario = session.query(Usuario).filter_by(email=email_usuario).first()

    if usuario:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
    else:
        print("Usuário não encontrado. ")
    return consultar_usuario
"""