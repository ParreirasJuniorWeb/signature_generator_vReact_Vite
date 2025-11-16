# 🏗️ Arquitetura do Sistema - Gerador de Assinaturas

## 📋 Visão Geral

Sistema completo para geração de assinaturas de e-mail, composto por:
- **Backend**: API REST em Flask (Python)
- **Frontend**: SPA em React + Vite + Tailwind CSS
- **Deploy**: Docker + Nginx

## 🎯 Princípios Arquiteturais

### 1. Separação de Responsabilidades
- Backend focado em lógica de negócio e geração de imagens
- Frontend focado em UX/UI e validação client-side
- Comunicação via API REST

### 2. Arquitetura em Camadas

#### Backend (Flask)
```
┌─────────────────────────────────────┐
│         API Layer (routes.py)       │  ← Endpoints REST
├─────────────────────────────────────┤
│      Service Layer (services/)      │  ← Lógica de Negócio
├─────────────────────────────────────┤
│       Utils Layer (utils/)          │  ← Utilitários
├─────────────────────────────────────┤
│     Constants (constants/)          │  ← Configurações
└─────────────────────────────────────┘
```

#### Frontend (React)
```
┌─────────────────────────────────────┐
│      Components (components/)       │  ← UI Components
├─────────────────────────────────────┤
│         Hooks (hooks/)              │  ← Custom Hooks
├─────────────────────────────────────┤
│       Services (services/)          │  ← API Communication
├─────────────────────────────────────┤
│         Utils (utils/)              │  ← Helpers
└─────────────────────────────────────┘
```

## 📁 Estrutura de Diretórios

```
signature_generator/
├── backend/                    # 🔧 API Flask
│   ├── app/
│   │   ├── api/               # Rotas e endpoints
│   │   ├── services/          # Lógica de negócio
│   │   ├── utils/             # Utilitários
│   │   └── constants/         # Constantes
│   ├── tests/                 # Testes automatizados
│   ├── static/                # Arquivos estáticos
│   └── run.py                 # Entry point
│
├── frontend/                   # ⚛️ React App
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   ├── hooks/             # Custom hooks
│   │   ├── services/          # Comunicação API
│   │   ├── utils/             # Utilitários
│   │   └── config/            # Configurações
│   └── public/                # Assets públicos
│
├── docker/                     # 🐳 Configurações Docker
│   ├── backend/
│   ├── frontend/
│   └── nginx/
│
└── docs/                       # 📚 Documentação
    ├── API.md
    ├── ARCHITECTURE.md
    └── DEPLOYMENT.md
```

## 🔄 Fluxo de Dados

### Geração de Assinatura

```
┌─────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│ Usuario │─────▶│ Frontend │─────▶│ Backend  │─────▶│  Pillow  │
│         │      │  (React) │      │  (Flask) │      │   (PIL)  │
└─────────┘      └──────────┘      └──────────┘      └──────────┘
     │                │                  │                  │
     │                │                  │                  │
     │           Validação          Validação          Geração
     │           Client-side        Server-side        Imagem
     │                │                  │                  │
     │                │                  │                  │
     │                │◀─────────────────┴──────────────────┘
     │                │           Imagem PNG
     │◀───────────────┘
     │    Download
```

### Detalhamento do Fluxo

1. **Frontend (React)**
   - Usuário preenche formulário
   - Validação em tempo real (client-side)
   - Formatação de dados (telefone, etc)
   - Envio via API

2. **Backend (Flask)**
   - Recebe dados via POST /api/signature
   - Valida com Marshmallow schemas
   - Valida com ValidationService
   - Normaliza com NormalizationService
   - Gera imagem com SignatureService (PIL)
   - Retorna imagem PNG

3. **Resposta**
   - Frontend recebe imagem
   - Exibe preview
   - Permite download

## 🔐 Segurança

### Backend
- ✅ Validação de entrada (Marshmallow)
- ✅ Sanitização de dados
- ✅ CORS configurado
- ✅ Tratamento de exceções
- ✅ Logs de segurança
- ✅ Rate limiting (via Nginx)

### Frontend
- ✅ Validação client-side
- ✅ Sanitização de entrada
- ✅ HTTPS (produção)
- ✅ CSP headers (via Nginx)

## 📊 Padrões de Projeto

### Backend

#### 1. Factory Pattern
```python
# app/__init__.py
def create_app(config_name):
    app = Flask(__name__)
    # Configuração...
    return app
```

#### 2. Service Layer Pattern
```python
# app/services/signature_service.py
class SignatureService:
    def generate_signature(self, data):
        # Lógica isolada
        pass
```

#### 3. Repository Pattern (Implícito)
- Separação entre lógica e dados
- Services acessam dados via utils

### Frontend

#### 1. Component Pattern
```jsx
// Componentes pequenos e reutilizáveis
<FormInput 
  name="fullName"
  label="Nome Completo"
  validation={validateName}
/>
```

#### 2. Custom Hooks Pattern
```jsx
// hooks/useSignatureForm.js
const useSignatureForm = () => {
  // Lógica reutilizável
  return { formData, handleSubmit, errors };
};
```

#### 3. Service Pattern
```javascript
// services/api.service.js
export const apiService = {
  generateSignature: (data) => axios.post('/signature', data)
};
```

## 🧪 Estratégia de Testes

### Backend (pytest)
```
tests/
├── test_api.py           # Testes de endpoints
├── test_services.py      # Testes de serviços
├── test_validators.py    # Testes de validação
└── conftest.py           # Fixtures
```

### Frontend (Vitest)
```
tests/
├── components/           # Testes de componentes
├── hooks/                # Testes de hooks
├── services/             # Testes de serviços
└── setup.js              # Configuração
```

## 🚀 Deploy

### Desenvolvimento
```bash
# Backend
cd backend
python run.py

# Frontend
cd frontend
npm run dev
```

### Produção (Docker)
```bash
docker-compose up -d
```

### Arquitetura de Deploy
```
┌──────────────────────────────────────────┐
│              Nginx (Port 80)             │
│  ┌────────────────┬──────────────────┐   │
│  │   Frontend     │    Backend       │   │
│  │   (Static)     │    (Proxy)       │   │
│  └────────────────┴──────────────────┘   │
└──────────────────────────────────────────┘
         │                    │
         │                    │
    ┌────▼────┐         ┌────▼────┐
    │ React   │         │  Flask  │
    │  App    │         │   API   │
    └─────────┘         └─────────┘
```

## 📈 Escalabilidade

### Horizontal
- Backend: Múltiplas instâncias via Gunicorn workers
- Frontend: CDN para assets estáticos
- Load balancer (Nginx)

### Vertical
- Otimização de imagens (PIL)
- Cache de fontes
- Compressão de resposta

## 🔧 Manutenibilidade

### Código Limpo
- Type hints (Python)
- PropTypes (React)
- Docstrings
- Comentários significativos

### Modularidade
- Componentes pequenos
- Serviços isolados
- Funções puras
- Baixo acoplamento

### Documentação
- README por módulo
- Documentação de API (Swagger)
- Guias de desenvolvimento
- Changelog

## 📝 Convenções

### Nomenclatura

#### Python (Backend)
```python
# snake_case para funções e variáveis
def validate_user_data(user_data):
    pass

# PascalCase para classes
class ValidationService:
    pass

# UPPER_CASE para constantes
MAX_FILE_SIZE = 1024
```

#### JavaScript (Frontend)
```javascript
// camelCase para funções e variáveis
const validateUserData = (userData) => {};

// PascalCase para componentes
const FormInput = () => {};

// UPPER_CASE para constantes
const API_URL = 'http://localhost:5000';
```

### Commits
```
feat: adiciona nova funcionalidade
fix: corrige bug
docs: atualiza documentação
style: formatação de código
refactor: refatoração
test: adiciona testes
chore: tarefas de manutenção
```

## 🔄 Versionamento

- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Branches**:
  - `main`: produção
  - `develop`: desenvolvimento
  - `feature/*`: novas features
  - `hotfix/*`: correções urgentes

## 📚 Referências

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Docker Documentation](https://docs.docker.com/)

---

**Última atualização**: 2024
**Versão**: 2.0.0
