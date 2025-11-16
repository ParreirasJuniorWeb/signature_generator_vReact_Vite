"""
Fixtures do pytest para testes.
Define fixtures reutilizáveis em todos os testes.
"""
import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Fixture que cria uma instância da aplicação para testes.
    
    Returns:
        Instância da aplicação Flask configurada para testes
    """
    app = create_app('testing')
    
    # Configurações adicionais para testes
    app.config.update({
        'TESTING': True,
    })
    
    yield app


@pytest.fixture
def client(app):
    """
    Fixture que cria um cliente de teste.
    
    Args:
        app: Fixture da aplicação
        
    Returns:
        Cliente de teste Flask
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Fixture que cria um runner CLI para testes.
    
    Args:
        app: Fixture da aplicação
        
    Returns:
        CLI runner
    """
    return app.test_cli_runner()


@pytest.fixture
def valid_user_data():
    """
    Fixture com dados válidos de usuário.
    
    Returns:
        Dicionário com dados válidos
    """
    return {
        'fullName': 'João Pedro Silva',
        'jobTitle': 'Desenvolvedor de Software',
        'department': 'ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO',
        'phoneNumber': '3139160000',
        'telephoneNumber': '31987654321',
        'email': 'joao.silva@saude.mg.gov.br',
        'adress': 'Cidade Administrativa, Prédio Minas, 1º andar'
    }


@pytest.fixture
def invalid_user_data():
    """
    Fixture com dados inválidos de usuário.
    
    Returns:
        Dicionário com dados inválidos
    """
    return {
        'fullName': 'Jo',  # Muito curto
        'jobTitle': 'Dev',  # Muito curto
        'department': 'TI',  # Muito curto
        'phoneNumber': '123',  # Formato inválido
        'email': 'invalid-email',  # E-mail inválido
        'adress': 'End'  # Muito curto
    }


@pytest.fixture
def sample_normalized_data():
    """
    Fixture com dados já normalizados.
    
    Returns:
        Dicionário com dados normalizados
    """
    return {
        'fullName': 'João Pedro Silva',
        'jobTitle': 'Desenvolvedor de Software',
        'department': 'ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO',
        'phoneNumber': '(31) 3916-0000',
        'telephoneNumber': '(31) 98765-4321',
        'email': 'joao.silva@saude.mg.gov.br',
        'adress': 'Cidade Administrativa, Prédio Minas, 1º Andar'
    }
