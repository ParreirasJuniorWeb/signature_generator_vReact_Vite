"""
Entry point da aplicação Flask.
Inicia o servidor de desenvolvimento ou produção.
"""
import os
from app import create_app

# Cria a aplicação
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    # Configurações do servidor
    host = app.config.get('HOST', '0.0.0.0')
    port = app.config.get('PORT', 5000)
    debug = app.config.get('DEBUG', False)
    
    app.logger.info(f"Iniciando servidor em {host}:{port}")
    app.logger.info(f"Modo debug: {debug}")
    
    # Inicia o servidor
    app.run(
        host=host,
        port=port,
        debug=debug
    )
