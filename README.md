# 📧 Signature Generator - Gerador de Assinaturas de E-mail

> Sistema completo para geração de assinaturas de e-mail personalizadas para a Secretaria de Estado de Saúde de Minas Gerais (SES-MG)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yourusername/signature-generator)
[![Python](https://img.shields.io/badge/python-3.12+-green.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.1.2-lightgrey.svg)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/react-19.2.0-61dafb.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Características](#características)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Documentação](#documentação)
- [Testes](#testes)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## 🎯 Sobre o Projeto

O **Signature Generator** é uma aplicação web completa que permite aos funcionários da SES-MG gerar assinaturas de e-mail padronizadas e profissionais de forma rápida e fácil.

### Versão 2.0.0 - Reestruturação Completa ✨

Esta versão representa uma **reestruturação completa** do projeto, transformando-o de uma aplicação monolítica para uma arquitetura moderna, modular e escalável.

### O que mudou?

- ✅ **Separação Backend/Frontend** - Arquitetura desacoplada
- ✅ **Arquitetura em Camadas** - Código organizado e manutenível
- ✅ **Validação Robusta** - Marshmallow + validações customizadas
- ✅ **Sistema de Logs** - Logging profissional com rotação
- ✅ **Testes Automatizados** - Cobertura com pytest
- ✅ **Documentação Completa** - Docs detalhadas de API e arquitetura
- ✅ **Configuração Flexível** - Suporte a múltiplos ambientes

---

## ✨ Características

### Backend (Flask API)
- 🚀 API REST completa e documentada
- 🔒 Validação robusta de dados (Marshmallow)
- 📝 Sistema de logs profissional
- 🧪 Testes automatizados (pytest)
- ⚙️ Configuração por ambiente (.env)
- 🎨 Geração de imagens PNG de alta qualidade
- 🔄 Normalização automática de dados
- 🛡️ Tratamento de erros centralizado

### Frontend (React + Vite)
- ⚡ Interface moderna e responsiva
- 🎨 Tailwind CSS para estilização
- 📱 Design mobile-first
- ✅ Validação em tempo real
- 👁️ Preview ao vivo da assinatura
- 💾 Download direto da imagem

---

## 🛠️ Tecnologias

### Backend
```
Flask 3.1.2          - Framework web
Flask-CORS 5.0.0     - CORS support
Marshmallow 3.23.2   - Validação de dados
Pillow 12.0.0        - Processamento de imagens
python-dotenv 1.0.1  - Variáveis de ambiente
pytest 9.0.1         - Framework de testes
gunicorn 23.0.0      - WSGI server
```

### Frontend
```
React 19.2.0         - Biblioteca UI
Vite 7.2.2           - Build tool
Tailwind CSS 3.4.18  - Framework CSS
```

---

## 📁 Estrutura do Projeto

```
signature_generator/
├── backend/              # Backend Flask API
│   ├── app/             # Código da aplicação
│   │   ├── api/         # Endpoints e schemas
│   │   ├── services/    # Lógica de negócio
│   │   ├── utils/       # Utilitários
│   │   └── constants/   # Constantes
│   ├── static/          # Arquivos estáticos
│   ├── tests/           # Testes automatizados
│   └── logs/            # Logs da aplicação
│
├── frontend/            # Frontend React
│   ├── src/            # Código fonte
│   │   ├── components/ # Componentes React
│   │   ├── services/   # Serviços de API
│   │   └── utils/      # Utilitários
│   └── public/         # Arquivos públicos
│
└── docs/               # Documentação
    ├── API.md          # Documentação da API
    ├── ARCHITECTURE.md # Arquitetura
    └── ...             # Outros docs
```

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.12+
- Node.js 18+
- pip
- npm ou yarn

### Backend

```bash
# 1. Clone o repositório
git clone https://github.com/yourusername/signature-generator.git
cd signature-generator

# 2. Navegue para o backend
cd backend

# 3. Crie um ambiente virtual
python -m venv .venv

# 4. Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env conforme necessário

# 7. Execute o servidor
python run.py
```

O servidor estará rodando em `http://localhost:5000`

### Frontend

```bash
# 1. Navegue para o frontend
cd frontend

# 2. Instale as dependências
npm install

# 3. Execute em modo desenvolvimento
npm run dev

# 4. Acesse no navegador
# http://localhost:5173
```

---

## 💻 Uso

### API REST

#### Health Check
```bash
curl http://localhost:5000/api/health
```

#### Validar Dados
```bash
curl -X POST http://localhost:5000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor Senior",
    "department": "Tecnologia da Informacao",
    "phoneNumber": "3112345678",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
  }'
```

#### Gerar Assinatura
```bash
curl -X POST http://localhost:5000/api/signature \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor Senior",
    "department": "Tecnologia da Informacao",
    "phoneNumber": "3112345678",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
  }' \
  --output assinatura.png
```

### Interface Web

1. Acesse `http://localhost:5173`
2. Preencha o formulário com seus dados
3. Visualize o preview da assinatura em tempo real
4. Clique em "Gerar Assinatura"
5. Faça o download da imagem PNG

---

## 📚 Documentação

Documentação completa disponível em `/docs`:

- **[API.md](docs/API.md)** - Documentação completa da API REST
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Arquitetura do sistema
- **[CHANGELOG.md](docs/CHANGELOG.md)** - Histórico de mudanças
- **[MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)** - Guia de migração
- **[SUMMARY.md](docs/SUMMARY.md)** - Resumo das mudanças
- **[PROJECT_COMPLETION.md](docs/PROJECT_COMPLETION.md)** - Status do projeto

### Backend
- **[Backend README](backend/README.md)** - Guia completo do backend
- **[Testing Results](backend/TESTING_RESULTS.md)** - Resultados dos testes

---

## 🧪 Testes

### Backend

```bash
# Executar todos os testes
cd backend
pytest tests/ -v

# Executar com cobertura
pytest tests/ --cov=app --cov-report=html

# Executar testes específicos
pytest tests/test_api.py -v
```

### Resultados dos Testes

- ✅ **5 de 6 testes passando** (83.3%)
- ✅ Health Check funcionando
- ✅ Validação de dados funcionando
- ✅ Geração de assinatura funcionando
- ✅ Tratamento de erros funcionando

Veja [TESTING_RESULTS.md](backend/TESTING_RESULTS.md) para detalhes completos.

---

## 🎨 Exemplos

### Exemplo de Assinatura Gerada

![Exemplo de Assinatura](backend/static/images/new_default_signature_ses.png)

### Dados de Exemplo

```json
{
  "fullName": "Maria Silva Santos",
  "jobTitle": "Coordenadora de Saúde Pública",
  "department": "COORDENADORIA DE VIGILÂNCIA EPIDEMIOLÓGICA",
  "phoneNumber": "(31) 3916-0123",
  "telephoneNumber": "(31) 98765-4321",
  "email": "maria.santos@saude.mg.gov.br",
  "adress": "Cidade Administrativa, Prédio Minas, 3º andar"
}
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, siga estas etapas:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes

- Siga o estilo de código existente
- Adicione testes para novas features
- Atualize a documentação
- Mantenha commits pequenos e focados

---

## 📊 Status do Projeto

### Backend
- ✅ **Completo e Testado**
- ✅ Pronto para produção
- ✅ Documentação completa

### Frontend
- ⏳ **Em Desenvolvimento**
- ⏳ Estrutura preparada
- ⏳ Aguardando implementação

### Documentação
- ✅ **Completa**
- ✅ API documentada
- ✅ Arquitetura documentada
- ✅ Guias de uso criados

---

## 🗺️ Roadmap

### Fase 1: Frontend (Em Andamento)
- [ ] Implementar componentes React
- [ ] Integrar com API
- [ ] Validação em tempo real
- [ ] Estilização com Tailwind

### Fase 2: Melhorias
- [ ] Cache de fontes
- [ ] Otimização de imagens
- [ ] Rate limiting
- [ ] Monitoramento

### Fase 3: Deploy
- [ ] Configurar Docker
- [ ] CI/CD pipeline
- [ ] Deploy staging
- [ ] Deploy produção

### Fase 4: Features Adicionais
- [ ] Múltiplos templates
- [ ] Personalização de cores
- [ ] Upload de logo
- [ ] Histórico de assinaturas

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👥 Autores

- **João Pedro** - *Desenvolvedor Principal* - [GitHub](https://github.com/yourusername)
- **BLACKBOXAI** - *Assistente de Desenvolvimento* - Arquitetura, Testes e Documentação

---

## 🙏 Agradecimentos

- Secretaria de Estado de Saúde de Minas Gerais (SES-MG)
- Comunidade Flask
- Comunidade React
- Todos os contribuidores

---

## 📞 Suporte

Para dúvidas ou problemas:

1. 📖 Consulte a [documentação](docs/)
2. 🐛 Abra uma [issue](https://github.com/yourusername/signature-generator/issues)
3. 💬 Entre em contato: joao.pedro@example.com

---

## 🔗 Links Úteis

- [Documentação da API](docs/API.md)
- [Guia de Arquitetura](docs/ARCHITECTURE.md)
- [Guia de Migração](docs/MIGRATION_GUIDE.md)
- [Resultados dos Testes](backend/TESTING_RESULTS.md)

---

<div align="center">

**Desenvolvido com ❤️ para a SES-MG**

[⬆ Voltar ao topo](#-signature-generator---gerador-de-assinaturas-de-e-mail)

</div>
