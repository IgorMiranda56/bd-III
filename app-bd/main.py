from services.usuario_services import UsuarioServices
from repositories.usuario_repositories import UsuarioRepositories
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepositories(session)
    service = UsuarioServices(repository)

    # Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    # Listar todos os usuários cadastrados.
    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.emai} - Senha: {usuario.senha}")

if __name__ == "__main__":
    main()
