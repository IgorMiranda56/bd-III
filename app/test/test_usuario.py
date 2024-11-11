import pytest
from app.models.usuario_model import Usuario

@pytest.fixture
def test_modelo(Usuario):
        return Usuario(nome = "Marta", email = "marta@gmail", senha = "123") 

def test_nome_vazio():
    with pytest.raises(ValueError, match="Nome não pode conter espaços vazios."):
        Usuario("", "marta@gamil.com", "123")
def test_nome_invalido():
    with pytest.raises(TypeError, match="Digite apenas texto para os nome."):
        Usuario(000, "marta@gamil.com", "123")

def test_email():
     with pytest.raises(ValueError, match="E-mail não pode conter espaços vazios."):
          Usuario("Marta", "", "123")

def test_senha():
     with pytest.raises(ValueError, match="Senha não pode conter espaços vazios."):
          Usuario("Marta", "marta@gmail.com", "")

def test_validar_nome():
    assert Usuario.nome == "Marta"

def test_validar_email():
    assert Usuario.email == "marta@gmail.com"

def test_validar_senha():
    assert Usuario.senha== "123"
