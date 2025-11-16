"""
Respostas padronizadas da API.
Define estruturas de resposta consistentes.
"""
from flask import jsonify
from typing import Any, Dict, Optional


def success_response(data: Any = None, message: str = "Sucesso", status_code: int = 200):
    """
    Cria uma resposta de sucesso padronizada.
    
    Args:
        data: Dados a serem retornados
        message: Mensagem de sucesso
        status_code: Código HTTP de status
        
    Returns:
        Tupla (response, status_code)
    """
    response = {
        "success": True,
        "message": message
    }
    
    if data is not None:
        response["data"] = data
    
    return jsonify(response), status_code


def error_response(
    message: str,
    status_code: int = 400,
    errors: Optional[Dict[str, str]] = None,
    details: Optional[str] = None
):
    """
    Cria uma resposta de erro padronizada.
    
    Args:
        message: Mensagem de erro
        status_code: Código HTTP de status
        errors: Dicionário de erros específicos por campo
        details: Detalhes adicionais do erro
        
    Returns:
        Tupla (response, status_code)
    """
    response = {
        "success": False,
        "error": message,
        "status_code": status_code
    }
    
    if errors:
        response["errors"] = errors
    
    if details:
        response["details"] = details
    
    return jsonify(response), status_code


def validation_error_response(errors: Dict[str, str]):
    """
    Cria uma resposta de erro de validação.
    
    Args:
        errors: Dicionário de erros de validação
        
    Returns:
        Tupla (response, status_code)
    """
    return error_response(
        message="Erro de validação",
        status_code=422,
        errors=errors
    )


def not_found_response(resource: str = "Recurso"):
    """
    Cria uma resposta de recurso não encontrado.
    
    Args:
        resource: Nome do recurso não encontrado
        
    Returns:
        Tupla (response, status_code)
    """
    return error_response(
        message=f"{resource} não encontrado",
        status_code=404
    )


def internal_error_response(message: str = "Erro interno do servidor"):
    """
    Cria uma resposta de erro interno.
    
    Args:
        message: Mensagem de erro
        
    Returns:
        Tupla (response, status_code)
    """
    return error_response(
        message=message,
        status_code=500
    )
