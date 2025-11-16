"""
Sistema de logging estruturado para a aplicação.
Configura logs para console e arquivo com rotação.
"""
import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime


class ColoredFormatter(logging.Formatter):
    """Formatter customizado com cores para o console."""
    
    # Códigos de cores ANSI
    COLORS = {
        'DEBUG': '\033[36m',      # Ciano
        'INFO': '\033[32m',       # Verde
        'WARNING': '\033[33m',    # Amarelo
        'ERROR': '\033[31m',      # Vermelho
        'CRITICAL': '\033[35m',   # Magenta
        'RESET': '\033[0m'        # Reset
    }
    
    def format(self, record):
        """Formata o log com cores."""
        log_color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        record.levelname = f"{log_color}{record.levelname}{self.COLORS['RESET']}"
        return super().format(record)


def setup_logger(app):
    """
    Configura o sistema de logging da aplicação.
    
    Args:
        app: Instância da aplicação Flask
    """
    # Remove handlers existentes
    app.logger.handlers.clear()
    
    # Configurar nível de log
    log_level = getattr(logging, app.config['LOG_LEVEL'].upper(), logging.INFO)
    app.logger.setLevel(log_level)
    
    # Formato dos logs
    log_format = (
        '%(asctime)s - %(name)s - %(levelname)s - '
        '[%(filename)s:%(lineno)d] - %(message)s'
    )
    
    # Handler para console (com cores)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_formatter = ColoredFormatter(log_format)
    console_handler.setFormatter(console_formatter)
    app.logger.addHandler(console_handler)
    
    # Handler para arquivo (com rotação)
    log_file = app.config['LOG_FILE']
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=app.config['LOG_MAX_BYTES'],
        backupCount=app.config['LOG_BACKUP_COUNT'],
        encoding='utf-8'
    )
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter(log_format)
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)
    
    # Log de inicialização
    app.logger.info('=' * 80)
    app.logger.info(f'Aplicação iniciada em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    app.logger.info(f'Ambiente: {app.config.get("ENV", "development")}')
    app.logger.info(f'Debug: {app.config.get("DEBUG", False)}')
    app.logger.info(f'Nível de log: {app.config["LOG_LEVEL"]}')
    app.logger.info('=' * 80)


def get_logger(name):
    """
    Retorna um logger configurado para um módulo específico.
    
    Args:
        name: Nome do módulo
        
    Returns:
        Logger configurado
    """
    return logging.getLogger(name)
