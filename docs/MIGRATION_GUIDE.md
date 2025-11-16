# 🔄 Guia de Migração - v1.0 para v2.0

## 📊 Resumo Executivo

Este documento descreve todas as mudanças realizadas na reestruturação completa do projeto Gerador de Assinaturas.

## 🎯 Objetivos da Reestruturação

1. ✅ Separar responsabilidades entre front-end e back-end
2. ✅ Criar arquitetura modular e escalável
3. ✅ Implementar testes automatizados
4. ✅ Melhorar manutenibilidade do código
5. ✅ Adicionar documentação completa
6. ✅ Preparar para produção

## 📁 Nova Estrutura de Diretórios

### Antes (v1.0)
```
signature_generator/
├── app.py
├── data_validation.py
├── normalizer.py
├── signature_generator.py
├── routes.py
├── client/
│   └── src/
│       ├── App.jsx
│       └── js/
└── templates/
```

### Depois (v2.0)
```
signature_generator/
├── backend/                    # 🔧 Back-end separado
│   ├── app/
│   │   ├── api/               # Rotas e endpoints
│   │   ├── services/          # Lógica de negócio
│   │   ├── utils/             # Utilitários
│   │   └── constants/         # Constantes
│   ├── tests/                 # Testes automatizados
│   └── static/                # Arquivos estáticos
│
├── frontend/                   # ⚛️ Front-end separado
│   ├── src/
│   │   ├── components/        # Componentes React
│   │   ├── hooks/             # Custom hooks
│   │   ├── services/          # Comunicação API
│   │   └── utils/             # Utilitários
│   └── public/
│
├── docker/                     # 🐳 Configurações Docker
├── docs/                       # 📚 Documentação
└── README.md
```

## 🔧 Mudanças no Back-end

### Arquivos Migrados

| Arquivo Antigo | Novo Local | Mudanças |
|----------------|------------|----------|
| `app.py` | `backend/app/__init__.py` + `backend/run.py` | Factory pattern |
| `data_validation.py` | `backend/app/services/validation_service.py` | Refatorado com Marshmallow |
| `normalizer.py` | `backend/app/services/normalization_service.py` | Melhorado |
| `signature_generator.py` | `backend/app/services/signature_service.py` | Refatorado |
| `routes.py` | `backend/app/api/routes.py` | Blueprints + error handlers |

### Novos Arquivos Criados

#### Configuração
- `backend/app/config.py` - Configurações por ambiente
- `backend/app/extensions.py` - Extensões Flask
- `backend/.env.example` - Template de variáveis de ambiente

#### API
- `backend/app/api/schemas.py` - Schemas Marshmallow
- `backend/app/api/responses.py` - Respostas padronizadas

#### Utilitários
- `backend/app/utils/logger.py` - Sistema de logging
- `backend/app/utils/exceptions.py` - Exceções customizadas
- `backend/app/utils/validators.py` - Validadores reutilizáveis

#### Constantes
- `backend/app/constants/fonts.py` - Configurações de fontes
- `backend/app/constants/colors.py` - Cores
- `backend/app/constants/coordinates.py` - Coordenadas

#### Testes
- `backend/pytest.ini` - Configuração pytest
- `backend/tests/conftest.py` - Fixtures
- `backend/tests/test_api.py` - Testes de API

#### Dependências
- `backend/requirements.txt` - Dependências de produção
- `backend/requirements-dev.txt` - Dependências de desenvolvimento

## ⚛️ Mudanças no Front-end

### Arquivos Migrados

| Arquivo Antigo | Novo Local | Mudanças |
|----------------|------------|----------|
| `client/src/App.jsx` | `frontend/src/App.jsx` | Refatorado (componentes) |
| `client/src/js/apiService.js` | `frontend/src/services/api.service.js` | Axios + interceptors |
| `client/src/js/validator.js` | `frontend/src/utils/validators.js` | Melhorado |
| `client/src/js/formatter.js` | `frontend/src/utils/formatters.js` | Corrigido |

### Novos Arquivos Criados

#### Configuração
- `frontend/src/config/api.config.js` - Configuração da API
- `frontend/.env.example` - Template de variáveis
- `frontend/vite.config.js` - Configuração Vite
- `frontend/tailwind.config.js` - Configuração Tailwind

#### Componentes (Planejados)
- `frontend/src/components/Form/SignatureForm.jsx`
- `frontend/src/components/Preview/SignaturePreview.jsx`
- `frontend/src/components/UI/Button.jsx`
- `frontend/src/components/UI/Loading.jsx`

#### Hooks (Planejados)
- `frontend/src/hooks/useSignatureForm.js`
- `frontend/src/hooks/useFormValidation.js`
- `frontend/src/hooks/useApi.js`

## 🔄 Mudanças de Código

### Backend

#### Antes (app.py)
```python
from flask import Flask
from routes.form import form_route
from routes.api import api_route

app = Flask(__name__)
app.register_blueprint(form_route)
app.register_blueprint(api_route)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)  # Duplicado!
```

#### Depois (app/__init__.py + run.py)
```python
# app/__init__.py
def create_app(config_name=None):
    app = Flask(__name__)
    config_class = get_config(config_name)
    app.config.from_object(config_class)
    
    setup_logger(app)
    init_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    
    return app

# run.py
app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
```

#### Antes (data_validation.py)
```python
def validateData(userData):
    mandatoryKeys = ['fullName', 'jobTitle', ...]
    patterns = {...}
    
    for key in mandatoryKeys:
        if key not in userData:
            return False, f"Campo '{key}' não encontrado"
    
    for key, pattern in patterns.items():
        if not re.fullmatch(pattern, value):
            return False, f"Formato inválido para '{key}'"
    
    return True, "Dados validados"
```

#### Depois (services/validation_service.py + api/schemas.py)
```python
# api/schemas.py
class SignatureRequestSchema(Schema):
    fullName = fields.Str(required=True, validate=validate.Length(min=5))
    
    @validates('fullName')
    def validate_full_name(self, value):
        pattern = r'^[A-Za-zÀ-ú\s]{5,}$'
        if not re.fullmatch(pattern, value):
            raise ValidationError('Nome inválido')

# services/validation_service.py
class ValidationService:
    @staticmethod
    def validate_user_data(user_data):
        is_valid, sanitized_data, errors = validate_and_sanitize(user_data)
        if not is_valid:
            raise InvalidDataError("Dados inválidos", errors=errors)
        return sanitized_data
```

### Frontend

#### Antes (App.jsx)
```jsx
function App() {
  const refFullName = useRef(null);
  // ... muitos refs
  
  const handleSubmit = async (e) => {
    // Lógica misturada com UI
    const userData = {
      fullName: refFullName.current.value,
      // ...
    };
    
    const imageBlob = await sendSignatureRequest(userData);
    // Manipulação direta do DOM
    refDivImg.current.innerHTML = ...;
  };
  
  return (
    // JSX gigante com tudo misturado
  );
}
```

#### Depois (Planejado)
```jsx
// App.jsx
function App() {
  return (
    <MainLayout>
      <SignatureForm />
      <SignaturePreview />
    </MainLayout>
  );
}

// components/Form/SignatureForm.jsx
function SignatureForm() {
  const { formData, handleSubmit, errors, isLoading } = useSignatureForm();
  
  return (
    <form onSubmit={handleSubmit}>
      <FormInput name="fullName" {...formData.fullName} />
      {/* ... */}
      <Button type="submit" loading={isLoading}>
        Gerar Assinatura
      </Button>
    </form>
  );
}

// hooks/useSignatureForm.js
function useSignatureForm() {
  const [formData, setFormData] = useState({});
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    // Lógica isolada
  };
  
  return { formData, handleSubmit, errors, isLoading };
}
```

## 🐛 Bugs Corrigidos

### Backend
1. ✅ **Duplicação de app.run()** - Removida linha duplicada
2. ✅ **Validações inconsistentes** - Unificadas com Marshmallow
3. ✅ **Tratamento de erros** - Centralizado e padronizado
4. ✅ **Logs inadequados** - Sistema robusto implementado

### Frontend
1. ✅ **URL incorreta** - `/http://localhost:5000/api/` → `http://localhost:5000/api`
2. ✅ **Formatadores quebrados** - Corrigida implementação
3. ✅ **Manipulação do DOM** - Substituída por React state
4. ✅ **Validações duplicadas** - Sincronizadas com backend

## 📚 Documentação Criada

1. ✅ **README.md** - Documentação principal
2. ✅ **backend/README.md** - Guia do backend
3. ✅ **docs/API.md** - Documentação completa da API
4. ✅ **docs/ARCHITECTURE.md** - Arquitetura do sistema
5. ✅ **docs/CHANGELOG.md** - Histórico de mudanças
6. ✅ **docs/MIGRATION_GUIDE.md** - Este documento

## 🧪 Testes Implementados

### Backend
```bash
# Executar testes
cd backend
pytest

# Com cobertura
pytest --cov=app --cov-report=html
```

### Frontend (Estrutura preparada)
```bash
# Executar testes
cd frontend
npm test

# Com UI
npm run test:ui
```

## 🚀 Como Migrar

### 1. Backup do Código Antigo
```bash
cp -r signature_generator signature_generator_v1_backup
```

### 2. Instalar Dependências do Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente
```bash
cp .env.example .env
# Editar .env com suas configurações
```

### 4. Copiar Arquivos Estáticos
```bash
# Copiar fontes e imagens do projeto antigo
cp -r signature_generator_old/static backend/static
```

### 5. Instalar Dependências do Frontend
```bash
cd frontend
npm install
```

### 6. Testar Localmente
```bash
# Terminal 1 - Backend
cd backend
python run.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### 7. Executar Testes
```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

## ⚠️ Breaking Changes

### API Endpoints

#### Antes
```
POST /api
```

#### Depois
```
GET  /api/health      # Novo
POST /api/signature   # Renomeado
POST /api/validate    # Novo
```

### Estrutura de Resposta

#### Antes
```json
{
  "erro": "Mensagem de erro"
}
```

#### Depois
```json
{
  "success": false,
  "error": "Mensagem de erro",
  "status_code": 400,
  "errors": {
    "campo": "Erro específico"
  }
}
```

## 📋 Checklist de Migração

- [ ] Backup do código antigo
- [ ] Instalar dependências do backend
- [ ] Configurar variáveis de ambiente
- [ ] Copiar arquivos estáticos (fontes, imagens)
- [ ] Instalar dependências do frontend
- [ ] Testar backend localmente
- [ ] Testar frontend localmente
- [ ] Executar testes automatizados
- [ ] Atualizar configurações do Docker
- [ ] Testar com Docker Compose
- [ ] Atualizar documentação específica do projeto
- [ ] Deploy em ambiente de staging
- [ ] Testes de aceitação
- [ ] Deploy em produção

## 🆘 Troubleshooting

### Backend não inicia
```bash
# Verificar variáveis de ambiente
cat .env

# Verificar logs
tail -f logs/app.log

# Verificar dependências
pip list
```

### Frontend não conecta com Backend
```bash
# Verificar configuração da API
cat frontend/.env

# Verificar CORS no backend
# Editar backend/.env
CORS_ORIGINS=http://localhost:5173
```

### Testes falhando
```bash
# Backend
cd backend
pytest -v  # Modo verbose

# Frontend
cd frontend
npm test -- --reporter=verbose
```

## 📞 Suporte

Para dúvidas ou problemas:
1. Consulte a documentação em `docs/`
2. Verifique os logs em `backend/logs/`
3. Entre em contato com a equipe de TI

---

**Versão**: 2.0.0
**Data**: 2024
**Autor**: Assessoria de Tecnologia da Informação
