"""
Configurações centralizadas da aplicação Flask.
Gerencia diferentes ambientes (development, production, testing).
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir / '.env')


class Config:
    """Configuração base da aplicação."""
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Server
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'https://signature-generator-v-react-vite-n4.vercel.app/').split(',')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = basedir / os.getenv('LOG_FILE', 'logs/app.log')
    LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', 10485760))  # 10MB
    LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', 5))
    
    # Image Generation
    SIGNATURE_WIDTH = int(os.getenv('SIGNATURE_WIDTH', 800))
    SIGNATURE_HEIGHT = int(os.getenv('SIGNATURE_HEIGHT', 641))
    IMAGE_FORMAT = os.getenv('IMAGE_FORMAT', 'PNG')
    
    # Paths
    STATIC_FOLDER = basedir / 'static'
    FONTS_FOLDER = STATIC_FOLDER / 'fonts'
    IMAGES_FOLDER = STATIC_FOLDER / 'images'
    SIGNATURE_TEMPLATE = IMAGES_FOLDER / 'new_default_signature_ses.png'
    
    # Upload
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))  # 16MB
    UPLOAD_FOLDER = basedir / os.getenv('UPLOAD_FOLDER', 'uploads')
    
    # Proxy (se necessário)
    HTTP_PROXY = os.getenv('HTTP_PROXY', '')
    HTTPS_PROXY = os.getenv('HTTPS_PROXY', '')
    NO_PROXY = os.getenv('NO_PROXY', 'localhost,127.0.0.1')
    
    @staticmethod
    def init_app(app):
        """Inicializa configurações específicas da aplicação."""
        # Cria diretórios necessários
        Config.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        Config.UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


class DevelopmentConfig(Config):
    """Configuração para ambiente de desenvolvimento."""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Configuração para ambiente de produção."""
    DEBUG = False
    TESTING = False
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        
        # Log para syslog em produção
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


class TestingConfig(Config):
    """Configuração para ambiente de testes."""
    TESTING = True
    DEBUG = True
    
    # Usa banco de dados em memória para testes
    LOG_FILE = basedir / 'logs/test.log'


# Dicionário de configurações
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(config_name=None):
    """
    Retorna a configuração apropriada baseada no ambiente.
    
    Args:
        config_name: Nome da configuração ('development', 'production', 'testing')
        
    Returns:
        Classe de configuração apropriada
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    return config.get(config_name, DevelopmentConfig)
