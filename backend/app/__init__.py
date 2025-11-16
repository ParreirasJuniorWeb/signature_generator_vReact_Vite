"""
Factory da aplicação Flask.
Cria e configura a aplicação usando o padrão Factory.
"""
from flask import Flask
from app.config import get_config
from app.extensions import init_extensions
from app.utils.logger import setup_logger
from app.utils.exceptions import SignatureGeneratorException
from app.api.responses import error_response


def create_app(config_name=None):
    """
    Factory para criar a aplicação Flask.
    
    Args:
        config_name: Nome da configuração ('development', 'production', 'testing')
        
    Returns:
        Instância configurada da aplicação Flask
    """
    # Cria a instância do Flask
    app = Flask(__name__)
    
    # Carrega a configuração
    config_class = get_config(config_name)
    app.config.from_object(config_class)
    
    # Inicializa a configuração
    config_class.init_app(app)
    
    # Configura o sistema de logging
    setup_logger(app)
    
    # Inicializa extensões
    init_extensions(app)
    
    # Registra blueprints
    register_blueprints(app)
    
    # Registra error handlers
    register_error_handlers(app)
    
    # Log de inicialização
    app.logger.info(f"Aplicação criada com configuração: {config_name or 'default'}")
    
    return app


def register_blueprints(app):
    """
    Registra todos os blueprints da aplicação.
    
    Args:
        app: Instância da aplicação Flask
    """
    from app.api import api_bp
    
    app.register_blueprint(api_bp)
    
    app.logger.info("Blueprints registrados com sucesso")


def register_error_handlers(app):
    """
    Registra handlers globais de erro.
    
    Args:
        app: Instância da aplicação Flask
    """
    
    @app.errorhandler(SignatureGeneratorException)
    def handle_signature_exception(error):
        """Handler para exceções customizadas da aplicação."""
        app.logger.error(f"SignatureGeneratorException: {error.message}")
        return error_response(
            message=error.message,
            status_code=error.status_code
        )
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """Handler para erro 404."""
        return error_response("Recurso não encontrado", 404)
    
    @app.errorhandler(500)
    def handle_internal_error(error):
        """Handler para erro 500."""
        app.logger.error(f"Erro interno: {str(error)}", exc_info=True)
        return error_response(
            "Erro interno do servidor. Por favor, contate o suporte.",
            500
        )
    
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        """Handler para erros não tratados."""
        app.logger.error(f"Erro não tratado: {str(error)}", exc_info=True)
        return error_response(
            "Ocorreu um erro inesperado. Por favor, contate o suporte.",
            500
        )
    
    app.logger.info("Error handlers registrados com sucesso")
