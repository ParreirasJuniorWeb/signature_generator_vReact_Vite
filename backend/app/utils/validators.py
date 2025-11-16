"""
Validadores reutilizáveis para a aplicação.
Contém funções de validação que podem ser usadas em diferentes partes do código.
"""
import re
from typing import Tuple, Dict, Any


# Padrões de validação
VALIDATION_PATTERNS = {
    'fullName': r'^[A-Za-zÀ-ú\s\']{5,}$',
    'jobTitle': r'^.{5,}$',
    'phoneNumber': r'^\d{10}$',
    'telephoneNumber': r'^\d{11}$',
    'email': r'^[a-zA-Z.]+@saude\.mg\.gov\.br$',
    'department': r'^.{5,}$',
    'adress': r'^[A-Za-zÀ-ú\s0-9.,ºª°\-\/\\]{5,}$'
}

# Campos obrigatórios
MANDATORY_FIELDS = ['fullName', 'jobTitle', 'department', 'phoneNumber', 'email', 'adress']

# Campos opcionais
OPTIONAL_FIELDS = ['telephoneNumber']


def validate_field(field_name: str, value: Any) -> Tuple[bool, str]:
    """
    Valida um campo específico.
    
    Args:
        field_name: Nome do campo
        value: Valor a ser validado
        
    Returns:
        Tupla (is_valid, error_message)
    """
    # Verifica se o campo é obrigatório e está vazio
    if field_name in MANDATORY_FIELDS:
        if not value or not str(value).strip():
            return False, f"O campo '{field_name}' é obrigatório e não pode estar vazio."
    
    # Se o campo é opcional e está vazio, é válido
    if field_name in OPTIONAL_FIELDS and not str(value).strip():
        return True, ""
    
    # Valida o padrão do campo
    pattern = VALIDATION_PATTERNS.get(field_name)
    if not pattern:
        return True, ""  # Se não há padrão definido, considera válido
    
    # Para telefones, remove caracteres não numéricos antes de validar
    if field_name in ['phoneNumber', 'telephoneNumber']:
        value = re.sub(r'\D', '', str(value))
    
    # Valida contra o padrão
    if not re.fullmatch(pattern, str(value)):
        return False, f"O formato do campo '{field_name}' é inválido."
    
    return True, ""


def validate_email(email: str) -> Tuple[bool, str]:
    """
    Valida especificamente um endereço de e-mail.
    
    Args:
        email: Endereço de e-mail
        
    Returns:
        Tupla (is_valid, error_message)
    """
    if not email or not email.strip():
        return False, "E-mail é obrigatório."
    
    pattern = VALIDATION_PATTERNS['email']
    if not re.fullmatch(pattern, email):
        return False, "E-mail deve ser do domínio @saude.mg.gov.br"
    
    return True, ""


def validate_phone(phone: str, field_name: str = 'phoneNumber') -> Tuple[bool, str]:
    """
    Valida um número de telefone.
    
    Args:
        phone: Número de telefone
        field_name: Nome do campo (phoneNumber ou telephoneNumber)
        
    Returns:
        Tupla (is_valid, error_message)
    """
    # Remove caracteres não numéricos
    clean_phone = re.sub(r'\D', '', phone)
    
    # Verifica o comprimento
    if field_name == 'phoneNumber' and len(clean_phone) != 10:
        return False, "Telefone fixo deve ter 10 dígitos (DDD + número)."
    
    if field_name == 'telephoneNumber' and len(clean_phone) != 11:
        return False, "Celular deve ter 11 dígitos (DDD + número)."
    
    return True, ""


def validate_user_data(user_data: Dict[str, Any]) -> Tuple[bool, Dict[str, str]]:
    """
    Valida todos os dados do usuário.
    
    Args:
        user_data: Dicionário com os dados do usuário
        
    Returns:
        Tupla (is_valid, errors_dict)
    """
    errors = {}
    
    # Verifica campos obrigatórios
    for field in MANDATORY_FIELDS:
        if field not in user_data:
            errors[field] = f"Campo obrigatório '{field}' não foi enviado."
            continue
        
        value = user_data.get(field)
        is_valid, error_msg = validate_field(field, value)
        if not is_valid:
            errors[field] = error_msg
    
    # Valida campos opcionais se presentes
    for field in OPTIONAL_FIELDS:
        if field in user_data and user_data[field]:
            value = user_data.get(field)
            is_valid, error_msg = validate_field(field, value)
            if not is_valid:
                errors[field] = error_msg
    
    return len(errors) == 0, errors


def sanitize_input(value: str) -> str:
    """
    Remove caracteres potencialmente perigosos de uma string.
    
    Args:
        value: String a ser sanitizada
        
    Returns:
        String sanitizada
    """
    if not value:
        return ""
    
    # Remove tags HTML
    value = re.sub(r'<[^>]*>', '', value)
    
    # Remove caracteres de controle
    value = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', value)
    
    return value.strip()


def validate_and_sanitize(user_data: Dict[str, Any]) -> Tuple[bool, Dict[str, Any], Dict[str, str]]:
    """
    Valida e sanitiza os dados do usuário.
    
    Args:
        user_data: Dicionário com os dados do usuário
        
    Returns:
        Tupla (is_valid, sanitized_data, errors)
    """
    # Sanitiza os dados
    sanitized_data = {}
    for key, value in user_data.items():
        if isinstance(value, str):
            sanitized_data[key] = sanitize_input(value)
        else:
            sanitized_data[key] = value
    
    # Valida os dados sanitizados
    is_valid, errors = validate_user_data(sanitized_data)
    
    return is_valid, sanitized_data, errors
