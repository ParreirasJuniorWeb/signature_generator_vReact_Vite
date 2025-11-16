"""
Exceções customizadas para a aplicação.
Define exceções específicas para diferentes tipos de erros.
"""


class SignatureGeneratorException(Exception):
    """Exceção base para erros da aplicação."""
    
    def __init__(self, message, status_code=500, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload
    
    def to_dict(self):
        """Converte a exceção para um dicionário."""
        rv = dict(self.payload or ())
        rv['error'] = self.message
        rv['status_code'] = self.status_code
        return rv


class ValidationError(SignatureGeneratorException):
    """Erro de validação de dados."""
    
    def __init__(self, message, field=None):
        super().__init__(message, status_code=400)
        self.field = field
    
    def to_dict(self):
        rv = super().to_dict()
        if self.field:
            rv['field'] = self.field
        return rv


class ImageGenerationError(SignatureGeneratorException):
    """Erro durante a geração da imagem."""
    
    def __init__(self, message, details=None):
        super().__init__(message, status_code=500)
        self.details = details
    
    def to_dict(self):
        rv = super().to_dict()
        if self.details:
            rv['details'] = self.details
        return rv


class FileNotFoundError(SignatureGeneratorException):
    """Erro quando arquivo não é encontrado."""
    
    def __init__(self, filename):
        message = f"Arquivo não encontrado: {filename}"
        super().__init__(message, status_code=404)
        self.filename = filename
    
    def to_dict(self):
        rv = super().to_dict()
        rv['filename'] = self.filename
        return rv


class ConfigurationError(SignatureGeneratorException):
    """Erro de configuração da aplicação."""
    
    def __init__(self, message):
        super().__init__(message, status_code=500)


class InvalidDataError(SignatureGeneratorException):
    """Erro quando dados recebidos são inválidos."""
    
    def __init__(self, message, errors=None):
        super().__init__(message, status_code=422)
        self.errors = errors or {}
    
    def to_dict(self):
        rv = super().to_dict()
        if self.errors:
            rv['errors'] = self.errors
        return rv
