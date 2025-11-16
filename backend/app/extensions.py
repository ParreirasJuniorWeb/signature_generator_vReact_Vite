"""
Extensões Flask centralizadas.
Inicializa extensões que serão usadas em toda a aplicação.
"""
from flask_cors import CORS

# Instância do CORS
cors = CORS()


def init_extensions(app):
    """
    Inicializa todas as extensões Flask.
    
    Args:
        app: Instância da aplicação Flask
    """
    # Configurar CORS
    cors.init_app(
        app,
        resources={
            r"/api/*": {
                "origins": app.config['CORS_ORIGINS'],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "expose_headers": ["Content-Type", "X-Total-Count"],
                "supports_credentials": True,
                "max_age": 3600
            }
        }
    )
