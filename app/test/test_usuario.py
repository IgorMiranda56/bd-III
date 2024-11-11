import pytest
from services.usuario_services import UsuarioServices
from app.models.usuario_model import Usuario

@pytest.fixture
def test_modelo(Usuario):
        return Usuario(nome = "Marta", email = "marta@gmail", senha = "123") 

def test_nome_vazio():
    with pytest.raises(ValueError, match="vazio"):
        Usuario("", "marta@gamil.com", "123")
def test_nome_invalido():
    with pytest.raises(TypeError, match="invalido"):
        Usuario(000, "marta@gamil.com", "123")
