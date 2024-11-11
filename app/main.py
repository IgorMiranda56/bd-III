import os
import time
import sys


# Adiciona o diretório 'app' como diretório padrão.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import services
from app.config.database import Session
from app.models.usuario_model import Usuario
from app.repositories.usuario_repositories import UsuarioRepositories
from app.services.usuario_services import UsuarioServices

#from requests import session
#from sqlalchemy.orm import sessionmaker, declarative_base
#from sqlalchemy import create_engine, Column, String, Integer



# os.system("cls || clear")
def main():
    #Session = sessionmaker(bind=db)
    session = Session()
    repository = UsuarioRepositories(session)
    service = UsuarioServices(repository)

def lista_usuario(self):
        print("lista de todos os usuários cadastrados.")
        lista_usuarios = service.listar_todos_usuarios()
        #self.session.query(Usuario).all()
        for usuario in lista_usuarios:
            print(
                f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
#db = create_engine("sqlite:///meubancoaluno.db")

os.system("cls || clear")


def menu():
    print(
        f"=== SENAI SOLUTION === \n1 - Adicionar usuário \n2 - Pesquisar um usuário \n3 - Atualizar dados de um usuário \n4 - Excluir um usuário \n5 - Exibir todos os usuários cadastrados \n0 - Sair"
    )


while True:
    menu()
    opcao = input("Digite uma das opções:")
    os.system("cls || clear")
    match (opcao):
        case "1":
            print("Solicitando dados para o usuário. ")
            #create_usuario()
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

        case "2":
            #print("Consultando os dados de apenas um usuário. ")
            #consultar_usuario()
            #lista_usuario()
            #services.consultar_usuario()

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

if __name__ == "__main__":
   main()

#session.close()
