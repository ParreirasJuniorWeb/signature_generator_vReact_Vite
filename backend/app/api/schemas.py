"""
Schemas de validação usando Marshmallow.
Define a estrutura esperada dos dados de entrada.
"""
from marshmallow import Schema, fields, validate, validates, ValidationError
import re


class SignatureRequestSchema(Schema):
    """Schema para validação da requisição de geração de assinatura."""
    
    fullName = fields.Str(
        required=True,
        validate=validate.Length(min=5),
        error_messages={
            'required': 'Nome completo é obrigatório',
            'invalid': 'Nome inválido'
        }
    )
    
    jobTitle = fields.Str(
        required=True,
        validate=validate.Length(min=5),
        error_messages={
            'required': 'Cargo é obrigatório',
            'invalid': 'Cargo inválido'
        }
    )
    
    department = fields.Str(
        required=True,
        validate=validate.Length(min=5),
        error_messages={
            'required': 'Departamento é obrigatório',
            'invalid': 'Departamento inválido'
        }
    )
    
    phoneNumber = fields.Str(
        required=True,
        error_messages={
            'required': 'Telefone é obrigatório',
            'invalid': 'Telefone inválido'
        }
    )
    
    telephoneNumber = fields.Str(
        required=False,
        allow_none=True,
        missing=None
    )
    
    email = fields.Email(
        required=True,
        error_messages={
            'required': 'E-mail é obrigatório',
            'invalid': 'E-mail inválido'
        }
    )
    
    adress = fields.Str(
        required=True,
        validate=validate.Length(min=5),
        error_messages={
            'required': 'Endereço é obrigatório',
            'invalid': 'Endereço inválido'
        }
    )
    
    @validates('fullName')
    def validate_full_name(self, value):
        """Valida o nome completo."""
        pattern = r'^[A-Za-zÀ-ú\s\']{5,}$'
        if not re.fullmatch(pattern, value):
            raise ValidationError('Nome deve conter apenas letras, espaços e apóstrofo (mínimo 5 caracteres)')
    
    @validates('email')
    def validate_email_domain(self, value):
        """Valida o domínio do e-mail."""
        pattern = r'^[a-zA-Z.]+@saude\.mg\.gov\.br$'
        if not re.fullmatch(pattern, value):
            raise ValidationError('E-mail deve ser do domínio @saude.mg.gov.br')
    
    @validates('phoneNumber')
    def validate_phone_number(self, value):
        """Valida o número de telefone."""
        # Remove caracteres não numéricos
        clean_phone = re.sub(r'\D', '', value)
        if len(clean_phone) != 10:
            raise ValidationError('Telefone deve ter 10 dígitos (DDD + número)')
    
    @validates('telephoneNumber')
    def validate_telephone_number(self, value):
        """Valida o número de celular."""
        if value:  # Apenas valida se foi fornecido
            clean_phone = re.sub(r'\D', '', value)
            if len(clean_phone) != 11:
                raise ValidationError('Celular deve ter 11 dígitos (DDD + número)')
    
    @validates('adress')
    def validate_address(self, value):
        """Valida o endereço."""
        pattern = r'^[A-Za-zÀ-ú\s0-9.,ºª°\-\/\\]{5,}$'
        if not re.fullmatch(pattern, value):
            raise ValidationError('Endereço contém caracteres inválidos')


# Instância do schema para uso nas rotas
signature_request_schema = SignatureRequestSchema()
