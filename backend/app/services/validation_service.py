"""
Serviço de validação de dados.
Centraliza toda a lógica de validação de dados do usuário.
"""
from typing import Dict, Any, Tuple
from app.utils.validators import validate_and_sanitize
from app.utils.exceptions import ValidationError, InvalidDataError
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ValidationService:
    """Serviço responsável pela validação de dados."""
    
    @staticmethod
    def validate_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Valida e sanitiza os dados do usuário.
        
        Args:
            user_data: Dicionário com os dados do usuário
            
        Returns:
            Dicionário com os dados validados e sanitizados
            
        Raises:
            InvalidDataError: Se os dados forem inválidos
        """
        logger.info("Iniciando validação dos dados do usuário")
        
        # Verifica se dados foram enviados
        if not user_data:
            logger.error("Nenhum dado foi recebido")
            raise ValidationError("Nenhum dado foi recebido")
        
        # Valida e sanitiza os dados
        is_valid, sanitized_data, errors = validate_and_sanitize(user_data)
        
        if not is_valid:
            logger.warning(f"Dados inválidos: {errors}")
            raise InvalidDataError(
                "Os dados enviados são inválidos",
                errors=errors
            )
        
        logger.info("Dados validados com sucesso")
        return sanitized_data
    
    @staticmethod
    def validate_required_fields(user_data: Dict[str, Any], required_fields: list) -> Tuple[bool, str]:
        """
        Valida se todos os campos obrigatórios estão presentes.
        
        Args:
            user_data: Dicionário com os dados
            required_fields: Lista de campos obrigatórios
            
        Returns:
            Tupla (is_valid, error_message)
        """
        missing_fields = []
        
        for field in required_fields:
            if field not in user_data or not str(user_data.get(field, '')).strip():
                missing_fields.append(field)
        
        if missing_fields:
            error_msg = f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"
            logger.warning(error_msg)
            return False, error_msg
        
        return True, ""
