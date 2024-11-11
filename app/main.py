import os
import time
import sys

# Adiciona o diretório 'app' como diretório padrão.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.config.database import Session
from app.models.usuario_model import Usuario
from app.repositories.usuario_repositories import UsuarioRepositories
from app.services.usuario_services import UsuarioServices


def main():
    session = Session()
    repository = UsuarioRepositories(session)
    service = UsuarioServices(repository)

    while True:
        print(
            f"=== SENAI SOLUTION === \n1 - Adicionar usuário \n2 - Pesquisar um usuário \n3 - Atualizar dados de um usuário \n4 - Excluir um usuário \n5 - Exibir todos os usuários cadastrados \n0 - Sair"
        )
        opcao = input("Digite uma das opções: ")

        os.system("cls || clear")

        match (opcao):
            case "1":
                print("Solicitando dados para o usuário. ")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

            case "2":
                print("Consultando os dados de apenas um usuário. ")
                service.consultar_usuario()

            case "3":
                print("\nAtualizando dados do usuário. ")
                service.atualizar_usuario()

            case "4":
                print("\nExcluindo os dados de um usuário. ")
                service.excluir_usuario()

            case "5":
                print("\nExibindo dados de todos os usuários.")
                repository.listar_usuarios()

            case "0":
                print(f"Sistema encerrado.")
                break

            case _:
                print("Opção inválida.")
                time.sleep(2)
                os.system("cls || clear")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
