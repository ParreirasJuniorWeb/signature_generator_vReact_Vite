# 🔧 Signature Generator - Backend

API REST em Flask para geração de assinaturas de e-mail personalizadas.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Testes](#testes)
- [Desenvolvimento](#desenvolvimento)

## 🎯 Visão Geral

Backend modular e escalável construído com Flask, seguindo as melhores práticas de desenvolvimento:

- ✅ Arquitetura em camadas (API, Services, Utils)
- ✅ Sistema de logging estruturado
- ✅ Tratamento de erros centralizado
- ✅ Validação robusta com Marshmallow
- ✅ Testes automatizados com pytest
- ✅ Configuração via variáveis de ambiente
- ✅ CORS configurado adequadamente
- ✅ Documentação completa

## 🏗️ Arquitetura

```
backend/
├── app/
│   ├── __init__.py          # Factory da aplicação
│   ├── config.py            # Configurações
│   ├── extensions.py        # Extensões Flask
│   ├── api/                 # Camada de API
│   │   ├── routes.py        # Rotas/Endpoints
│   │   ├── schemas.py       # Schemas de validação
│   │   └── responses.py     # Respostas padronizadas
│   ├── services/            # Lógica de negócio
│   │   ├── signature_service.py
│   │   ├── validation_service.py
│   │   └── normalization_service.py
│   ├── utils/               # Utilitários
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── validators.py
│   └── constants/           # Constantes
│       ├── fonts.py
│       ├── colors.py
│       └── coordinates.py
├── tests/                   # Testes
├── static/                  # Arquivos estáticos
│   ├── fonts/
│   └── images/
├── run.py                   # Entry point
└── requirements.txt         # Dependências
```

### Camadas da Aplicação

1. **API Layer** (`app/api/`)
   - Define rotas e endpoints
   - Valida entrada com schemas
   - Retorna respostas padronizadas

2. **Service Layer** (`app/services/`)
   - Contém lógica de negócio
   - Independente do framework
   - Reutilizável e testável

3. **Utils Layer** (`app/utils/`)
   - Funções auxiliares
   - Validadores
   - Exceções customizadas
   - Sistema de logging

## 🚀 Instalação

### Pré-requisitos

- Python 3.10+
- pip
- virtualenv (recomendado)

### Passos

1. **Clone o repositório**
```bash
cd backend
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

Para desenvolvimento:
```bash
pip install -r requirements-dev.txt
```

## ⚙️ Configuração

### Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Server Configuration
HOST=0.0.0.0
PORT=5000
DEBUG=True

# CORS Configuration
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### Arquivos Estáticos

Certifique-se de que os seguintes arquivos estão presentes:

```
static/
├── fonts/
│   ├── arial.ttf
│   ├── arialbd.ttf
│   ├── ariblk.ttf
│   └── arialnb.TTF
└── images/
    └── new_default_signature_ses.png
```

## 🎮 Uso

### Desenvolvimento

```bash
python run.py
```

Ou usando Flask CLI:
```bash
flask run
```

### Produção

Com Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

## 📡 API Endpoints

### Health Check

```http
GET /api/health
```

**Resposta:**
```json
{
  "success": true,
  "message": "API está funcionando corretamente",
  "data": {
    "status": "healthy",
    "service": "Signature Generator API",
    "version": "2.0.0"
  }
}
```

### Gerar Assinatura

```http
POST /api/signature
Content-Type: application/json
```

**Request Body:**
```json
{
  "fullName": "João Pedro Silva",
  "jobTitle": "Desenvolvedor de Software",
  "department": "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
  "phoneNumber": "3139160000",
  "telephoneNumber": "31987654321",
  "email": "joao.silva@saude.mg.gov.br",
  "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
}
```

**Resposta:** Imagem PNG (binary)

**Erros:**
```json
{
  "success": false,
  "error": "Mensagem de erro",
  "status_code": 400,
  "errors": {
    "fullName": "Nome deve conter apenas letras"
  }
}
```

### Validar Dados

```http
POST /api/validate
Content-Type: application/json
```

**Request Body:** Mesmo formato do `/api/signature`

**Resposta:**
```json
{
  "success": true,
  "message": "Dados validados com sucesso",
  "data": {
    "fullName": "João Pedro Silva",
    ...
  }
}
```

## 🧪 Testes

### Executar todos os testes

```bash
pytest
```

### Executar com cobertura

```bash
pytest --cov=app --cov-report=html
```

### Executar testes específicos

```bash
pytest tests/test_api.py
pytest tests/test_services.py -v
```

### Executar por marcadores

```bash
pytest -m unit
pytest -m integration
```

## 🛠️ Desenvolvimento

### Estrutura de Código

- Use **type hints** em todas as funções
- Docstrings no formato Google
- Siga PEP 8
- Máximo 100 caracteres por linha

### Adicionar Nova Rota

1. Defina o schema em `app/api/schemas.py`
2. Crie a rota em `app/api/routes.py`
3. Implemente a lógica em `app/services/`
4. Adicione testes em `tests/`

### Logging

```python
from app.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("Mensagem informativa")
logger.warning("Aviso")
logger.error("Erro", exc_info=True)
```

### Exceções Customizadas

```python
from app.utils.exceptions import ValidationError

raise ValidationError("Dados inválidos", field="email")
```

### Code Quality

```bash
# Formatação
black app/

# Linting
flake8 app/
pylint app/

# Type checking
mypy app/
```

## 📝 Logs

Os logs são salvos em:
- Console (com cores)
- Arquivo: `logs/app.log` (com rotação)

Níveis de log:
- DEBUG: Informações detalhadas
- INFO: Informações gerais
- WARNING: Avisos
- ERROR: Erros
- CRITICAL: Erros críticos

## 🔒 Segurança

- Validação de entrada em todas as rotas
- Sanitização de dados
- CORS configurado
- Logs de segurança
- Tratamento de erros sem expor detalhes internos

## 📚 Dependências Principais

- **Flask 3.1.2**: Framework web
- **Flask-CORS 5.0.0**: Suporte a CORS
- **Pillow 12.0.0**: Processamento de imagens
- **Marshmallow 3.23.2**: Validação de dados
- **Gunicorn 23.0.0**: WSGI server
- **pytest 8.3.4**: Framework de testes

## 🤝 Contribuindo

1. Crie uma branch para sua feature
2. Implemente as mudanças
3. Adicione testes
4. Execute os testes
5. Faça commit das mudanças
6. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença especificada no arquivo LICENSE.

## 👥 Autores

- Desenvolvido pela Assessoria de Tecnologia da Informação
- Refatorado e melhorado por BLACKBOXAI

## 📞 Suporte

Para suporte, entre em contato com a equipe de TI.
