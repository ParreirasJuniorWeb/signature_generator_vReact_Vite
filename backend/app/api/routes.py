"""
Rotas da API REST.
Define os endpoints da aplicação.
"""
from flask import Blueprint, request, send_file, current_app
from marshmallow import ValidationError as MarshmallowValidationError

from app.api.responses import (
    success_response,
    error_response,
    validation_error_response,
    internal_error_response
)
from app.api.schemas import signature_request_schema
from app.services import (
    SignatureService,
    ValidationService,
    NormalizationService
)
from app.utils.exceptions import (
    SignatureGeneratorException,
    ValidationError,
    InvalidDataError,
    ImageGenerationError
)
from app.utils.logger import get_logger

logger = get_logger(__name__)

# Cria o Blueprint da API
api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint de health check.
    
    Returns:
        JSON com status da aplicação
    """
    return success_response(
        data={
            'status': 'healthy',
            'service': 'Signature Generator API',
            'version': '2.0.0'
        },
        message='API está funcionando corretamente'
    )


@api_bp.route('/signature', methods=['POST'])
def generate_signature():
    """
    Gera uma assinatura de e-mail.
    
    Request Body:
        {
            "fullName": "Nome Completo",
            "jobTitle": "Cargo",
            "department": "DEPARTAMENTO",
            "phoneNumber": "(31) 3916-0000",
            "telephoneNumber": "(31) 98765-4321",  // opcional
            "email": "nome.sobrenome@saude.mg.gov.br",
            "adress": "Endereço completo"
        }
    
    Returns:
        Imagem PNG da assinatura ou JSON com erro
    """
    try:
        # 1. Obtém os dados da requisição
        user_data = request.get_json()
        
        if not user_data:
            logger.warning("Requisição sem dados")
            return error_response("Nenhum dado foi recebido", 400)
        
        logger.info(f"Recebida requisição de geração de assinatura")
        
        # 2. Valida os dados usando Marshmallow
        try:
            validated_data = signature_request_schema.load(user_data)
        except MarshmallowValidationError as e:
            logger.warning(f"Erro de validação Marshmallow: {e.messages}")
            return validation_error_response(e.messages)
        
        # 3. Validação adicional com o serviço
        validation_service = ValidationService()
        validated_data = validation_service.validate_user_data(validated_data)
        
        # 4. Normaliza os dados
        normalization_service = NormalizationService()
        normalized_data = normalization_service.normalize_user_data(validated_data)
        
        # 5. Gera a assinatura
        signature_service = SignatureService(current_app.config)
        image_buffer = signature_service.generate_signature(normalized_data)
        
        # 6. Retorna a imagem
        logger.info("Assinatura gerada e enviada com sucesso")
        return send_file(
            image_buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name='assinatura.png'
        )
    
    except InvalidDataError as e:
        logger.warning(f"Dados inválidos: {e.message}")
        return error_response(
            message=e.message,
            status_code=e.status_code,
            errors=e.errors
        )
    
    except ValidationError as e:
        logger.warning(f"Erro de validação: {e.message}")
        return error_response(
            message=e.message,
            status_code=e.status_code
        )
    
    except ImageGenerationError as e:
        logger.error(f"Erro ao gerar imagem: {e.message}")
        return error_response(
            message=e.message,
            status_code=e.status_code,
            details=e.details
        )
    
    except SignatureGeneratorException as e:
        logger.error(f"Erro da aplicação: {e.message}")
        return error_response(
            message=e.message,
            status_code=e.status_code
        )
    
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}", exc_info=True)
        return internal_error_response(
            "Ocorreu um erro interno no servidor. Por favor, contate o suporte."
        )


@api_bp.route('/validate', methods=['POST'])
def validate_data():
    """
    Valida os dados sem gerar a assinatura.
    Útil para validação em tempo real no front-end.
    
    Request Body:
        Mesma estrutura do endpoint /signature
    
    Returns:
        JSON com resultado da validação
    """
    try:
        user_data = request.get_json()
        
        if not user_data:
            return error_response("Nenhum dado foi recebido", 400)
        
        # Valida usando Marshmallow
        try:
            validated_data = signature_request_schema.load(user_data)
        except MarshmallowValidationError as e:
            return validation_error_response(e.messages)
        
        # Validação adicional
        validation_service = ValidationService()
        validated_data = validation_service.validate_user_data(validated_data)
        
        return success_response(
            data=validated_data,
            message="Dados validados com sucesso"
        )
    
    except InvalidDataError as e:
        return error_response(
            message=e.message,
            status_code=e.status_code,
            errors=e.errors
        )
    
    except Exception as e:
        logger.error(f"Erro ao validar dados: {str(e)}")
        return internal_error_response()


# Error handlers para o Blueprint
@api_bp.errorhandler(404)
def not_found(error):
    """Handler para erro 404."""
    return error_response("Endpoint não encontrado", 404)


@api_bp.errorhandler(405)
def method_not_allowed(error):
    """Handler para erro 405."""
    return error_response("Método não permitido", 405)


@api_bp.errorhandler(500)
def internal_error(error):
    """Handler para erro 500."""
    logger.error(f"Erro interno: {str(error)}")
    return internal_error_response()
