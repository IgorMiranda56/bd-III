from config.database import Session
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from services.usuario_services import UsuarioServices
from repositories.usuario_repositories import UsuarioRepositories
import os
import time


BANCO = create_engine("sqlite:///meubancoaluno.db")

Session = sessionmaker(bind=BANCO)
session = Session()

Base = declarative_base()

os.system("cls || clear")
repository = UsuarioRepositories(session)
service = UsuarioServices(repository)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


Base.metadata.create_all(bind=BANCO)

os.system("cls || clear")


def menu():
    print(
        f"=== SENAI SOLUTION === \n1 - Adicionar usuário \n2 - Pesquisar um usuário \n3 - Atualizar dados de um usuário \n4 - Excluir um usuário \n5 - Exibir todos os usuários cadastrados \n0 - Sair"
    )

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
"""
"""
def read_usuario():
    lista_usuarios = session.query(Usuario).all()

    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")

    return read_usuario
"""

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


while True:
    menu()
    opcao = input("Digite uma das opções:")
    os.system("cls || clear")
    match (opcao):
        case "1":
            print("Solicitando dados para o usuário. ")
            create_usuario()

        case "2":
            print("Consultando os dados de apenas um usuário. ")
            consultar_usuario()

        case "3":
            print("\nAtualizando dados do usuário. ")
            update_usuario()

        case "4":
            print("\nExcluindo os dados de um usuário. ")
            delete_usuario()

        case "5":
            print("\nExibindo dados de todos os usuários.")
            read_usuario()

        case "0":
            print(f"Sistema encerrado.")
            break

        case _:
            print("Opção inválida.")
            time.sleep(2)
            os.system("cls || clear")

session.close()
