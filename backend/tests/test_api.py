"""
Testes para as rotas da API.
"""
import pytest
import json


class TestHealthCheck:
    """Testes para o endpoint de health check."""
    
    def test_health_check_success(self, client):
        """Testa se o health check retorna sucesso."""
        response = client.get('/api/health')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
        assert 'status' in data['data']
        assert data['data']['status'] == 'healthy'


class TestSignatureGeneration:
    """Testes para o endpoint de geração de assinatura."""
    
    def test_generate_signature_without_data(self, client):
        """Testa geração sem enviar dados."""
        response = client.post('/api/signature')
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert data['success'] is False
    
    def test_generate_signature_with_invalid_data(self, client, invalid_user_data):
        """Testa geração com dados inválidos."""
        response = client.post(
            '/api/signature',
            data=json.dumps(invalid_user_data),
            content_type='application/json'
        )
        
        assert response.status_code in [400, 422]
        data = json.loads(response.data)
        assert data['success'] is False
        assert 'error' in data
    
    def test_generate_signature_with_valid_data(self, client, valid_user_data):
        """Testa geração com dados válidos."""
        response = client.post(
            '/api/signature',
            data=json.dumps(valid_user_data),
            content_type='application/json'
        )
        
        # Deve retornar uma imagem PNG
        assert response.status_code == 200
        assert response.content_type == 'image/png'
        assert len(response.data) > 0


class TestValidation:
    """Testes para o endpoint de validação."""
    
    def test_validate_with_valid_data(self, client, valid_user_data):
        """Testa validação com dados válidos."""
        response = client.post(
            '/api/validate',
            data=json.dumps(valid_user_data),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['success'] is True
    
    def test_validate_with_invalid_data(self, client, invalid_user_data):
        """Testa validação com dados inválidos."""
        response = client.post(
            '/api/validate',
            data=json.dumps(invalid_user_data),
            content_type='application/json'
        )
        
        assert response.status_code in [400, 422]
        data = json.loads(response.data)
        assert data['success'] is False
