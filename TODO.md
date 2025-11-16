# 📋 TODO - Reestruturação do Signature Generator

## Status Geral: 🚧 Em Progresso

---

## 🔧 BACK-END

### 1. Estrutura de Diretórios
- [ ] Criar estrutura backend/app/
- [ ] Criar backend/app/api/
- [ ] Criar backend/app/services/
- [ ] Criar backend/app/utils/
- [ ] Criar backend/app/constants/
- [ ] Criar backend/tests/
- [ ] Criar backend/static/

### 2. Configuração e Inicialização
- [ ] Criar backend/app/config.py (configurações centralizadas)
- [ ] Criar backend/app/extensions.py (CORS, etc)
- [ ] Criar backend/app/__init__.py (factory pattern)
- [ ] Criar backend/run.py (entry point)
- [ ] Criar backend/.env.example

### 3. Camada de API
- [ ] Criar backend/app/api/routes.py
- [ ] Criar backend/app/api/schemas.py (Marshmallow)
- [ ] Criar backend/app/api/responses.py

### 4. Camada de Serviços
- [ ] Criar backend/app/services/signature_service.py
- [ ] Criar backend/app/services/validation_service.py
- [ ] Criar backend/app/services/normalization_service.py

### 5. Utilitários
- [ ] Criar backend/app/utils/logger.py
- [ ] Criar backend/app/utils/exceptions.py
- [ ] Criar backend/app/utils/validators.py

### 6. Constantes
- [ ] Criar backend/app/constants/fonts.py
- [ ] Criar backend/app/constants/colors.py
- [ ] Criar backend/app/constants/coordinates.py

### 7. Testes
- [ ] Criar backend/tests/conftest.py
- [ ] Criar backend/tests/test_api.py
- [ ] Criar backend/tests/test_services.py
- [ ] Criar backend/tests/test_validators.py
- [ ] Criar backend/pytest.ini

### 8. Dependências
- [ ] Atualizar backend/requirements.txt
- [ ] Criar backend/requirements-dev.txt

---

## ⚛️ FRONT-END

### 1. Estrutura de Diretórios
- [ ] Criar frontend/src/components/
- [ ] Criar frontend/src/hooks/
- [ ] Criar frontend/src/services/
- [ ] Criar frontend/src/utils/
- [ ] Criar frontend/src/config/
- [ ] Criar frontend/src/styles/
- [ ] Criar frontend/tests/

### 2. Componentes
- [ ] Criar frontend/src/components/Form/SignatureForm.jsx
- [ ] Criar frontend/src/components/Form/FormInput.jsx
- [ ] Criar frontend/src/components/Preview/SignaturePreview.jsx
- [ ] Criar frontend/src/components/Layout/Header.jsx
- [ ] Criar frontend/src/components/Layout/Footer.jsx
- [ ] Criar frontend/src/components/Layout/MainLayout.jsx
- [ ] Criar frontend/src/components/UI/Button.jsx
- [ ] Criar frontend/src/components/UI/Loading.jsx
- [ ] Criar frontend/src/components/UI/ErrorMessage.jsx

### 3. Custom Hooks
- [ ] Criar frontend/src/hooks/useSignatureForm.js
- [ ] Criar frontend/src/hooks/useFormValidation.js
- [ ] Criar frontend/src/hooks/useApi.js

### 4. Serviços
- [ ] Criar frontend/src/services/api.service.js
- [ ] Criar frontend/src/services/download.service.js

### 5. Utilitários
- [ ] Criar frontend/src/utils/validators.js
- [ ] Criar frontend/src/utils/formatters.js
- [ ] Criar frontend/src/utils/constants.js

### 6. Configuração
- [ ] Criar frontend/src/config/api.config.js
- [ ] Criar frontend/.env.example
- [ ] Atualizar frontend/vite.config.js
- [ ] Criar frontend/tailwind.config.js

### 7. Refatoração
- [ ] Refatorar frontend/src/App.jsx
- [ ] Atualizar frontend/src/main.jsx

### 8. Testes
- [ ] Criar frontend/tests/setup.js
- [ ] Criar frontend/vitest.config.js

### 9. Dependências
- [ ] Atualizar frontend/package.json

---

## 🐳 DOCKER

### 1. Dockerfiles
- [ ] Criar docker/backend/Dockerfile
- [ ] Criar docker/frontend/Dockerfile
- [ ] Criar docker/nginx/Dockerfile

### 2. Configuração Nginx
- [ ] Criar docker/nginx/nginx.conf

### 3. Docker Compose
- [ ] Atualizar docker-compose.yml
- [ ] Criar docker-compose.dev.yml

---

## 📚 DOCUMENTAÇÃO

### 1. Documentação da API
- [ ] Criar docs/API.md
- [ ] Adicionar Swagger/OpenAPI ao backend

### 2. Documentação Técnica
- [ ] Criar docs/ARCHITECTURE.md
- [ ] Criar docs/DEPLOYMENT.md
- [ ] Criar docs/CHANGELOG.md

### 3. README
- [ ] Atualizar README.md principal

---

## 🧪 TESTES E VALIDAÇÃO

- [ ] Executar testes do backend
- [ ] Executar testes do frontend
- [ ] Testar build de produção
- [ ] Testar deploy com Docker
- [ ] Validar todas as funcionalidades

---

## 📝 NOTAS

- Manter funcionalidade atual durante migração
- Garantir compatibilidade com deploy existente
- Documentar todas as mudanças
- Criar exemplos de uso

---

**Última atualização:** 2024-01-XX
**Responsável:** BLACKBOXAI
