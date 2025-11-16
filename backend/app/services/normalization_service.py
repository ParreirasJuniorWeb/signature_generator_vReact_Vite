"""
Serviço de normalização de dados.
Formata e padroniza os dados do usuário antes da geração da assinatura.
"""
import re
from typing import Dict, Any
from app.utils.logger import get_logger

logger = get_logger(__name__)


class NormalizationService:
    """Serviço responsável pela normalização de dados."""
    
    @staticmethod
    def capitalize_text(text: str) -> str:
        """
        Capitaliza texto respeitando artigos e preposições.
        
        Args:
            text: Texto a ser capitalizado
            
        Returns:
            Texto capitalizado
        """
        articles_prepositions = ['De', 'Da', 'Das', 'Do', 'Dos', 'E', 'Em']
        text = text.lower().title()
        
        for word in articles_prepositions:
            pattern = r'\b' + re.escape(word) + r'\b'
            text = re.sub(pattern, word.lower(), text, flags=re.IGNORECASE)
        
        return text
    
    @staticmethod
    def format_phone_number(phone: str) -> str:
        """
        Formata número de telefone.
        
        Args:
            phone: Número de telefone
            
        Returns:
            Telefone formatado
        """
        # Remove caracteres não numéricos
        cleaned_phone = re.sub(r'\D', '', phone)
        length = len(cleaned_phone)
        
        if length == 11:  # Celular: (XX) XXXXX-XXXX
            return re.sub(r'(\d{2})(\d{5})(\d{4})', r'(\1) \2-\3', cleaned_phone)
        elif length == 10:  # Fixo: (XX) XXXX-XXXX
            return re.sub(r'(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', cleaned_phone)
        elif length == 8:  # Fixo sem DDD: XXXX-XXXX
            return re.sub(r'(\d{4})(\d{4})', r'\1-\2', cleaned_phone)
        else:
            return phone
    
    @staticmethod
    def normalize_address(text: str) -> str:
        """
        Normaliza endereço mantendo siglas em maiúsculo.
        
        Args:
            text: Endereço a ser normalizado
            
        Returns:
            Endereço normalizado
        """
        normalized_text = NormalizationService.capitalize_text(text)
        acronyms = ['Bh', 'Mg', 'Srs', 'Grs']
        
        for acronym in acronyms:
            pattern = r'\b' + re.escape(acronym) + r'\b'
            normalized_text = re.sub(pattern, acronym.upper(), normalized_text)
        
        return normalized_text
    
    @staticmethod
    def normalize_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normaliza todos os dados do usuário.
        
        Args:
            user_data: Dicionário com os dados do usuário
            
        Returns:
            Dicionário com os dados normalizados
        """
        logger.info("Iniciando normalização dos dados")
        
        normalized_data = user_data.copy()
        
        for key, value in normalized_data.items():
            if not isinstance(value, str):
                continue
            
            if key in ['fullName', 'jobTitle']:
                normalized_data[key] = NormalizationService.capitalize_text(value)
            elif key == 'department':
                normalized_data[key] = value.upper()
            elif key in ['phoneNumber', 'telephoneNumber']:
                normalized_data[key] = NormalizationService.format_phone_number(value)
            elif key == 'adress':
                normalized_data[key] = NormalizationService.normalize_address(value)
            elif key == 'email':
                normalized_data[key] = value.lower()
        
        logger.info("Dados normalizados com sucesso")
        return normalized_data
