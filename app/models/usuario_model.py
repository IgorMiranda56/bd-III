from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))
    
    # Definindo características da classe. 
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def _verificar_nome(self, nome: str):
        if not isinstance(nome, str):
            raise TypeError("Digite apenas texto para os nome.")
        if not nome.strip():
            raise ValueError("Nome não pode conter espaços vazios.")
        return nome

    def _verificar_email(self, email: str):
        if not email.strip():
            raise ValueError("E-mail não pode conter espaços vazios.")
        return email

    def _verificar_senha(self, senha: str):
        if not senha.strip():
            raise ValueError("Senha não pode conter espaços vazios.")
        return senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)