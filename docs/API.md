# 📡 Documentação da API - Gerador de Assinaturas

## Base URL

```
http://localhost:5000/api
```

## Autenticação

Atualmente a API não requer autenticação.

## Headers Padrão

```http
Content-Type: application/json
Accept: application/json
```

## Respostas Padrão

### Sucesso
```json
{
  "success": true,
  "message": "Mensagem de sucesso",
  "data": {}
}
```

### Erro
```json
{
  "success": false,
  "error": "Mensagem de erro",
  "status_code": 400,
  "errors": {
    "campo": "Mensagem específica do erro"
  }
}
```

## Endpoints

### 1. Health Check

Verifica se a API está funcionando.

**Endpoint:** `GET /api/health`

**Resposta de Sucesso (200)**
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

**Exemplo cURL:**
```bash
curl -X GET http://localhost:5000/api/health
```

---

### 2. Gerar Assinatura

Gera uma assinatura de e-mail personalizada.

**Endpoint:** `POST /api/signature`

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

**Campos:**

| Campo | Tipo | Obrigatório | Descrição | Validação |
|-------|------|-------------|-----------|-----------|
| fullName | string | Sim | Nome completo | Mínimo 5 caracteres, apenas letras |
| jobTitle | string | Sim | Cargo/função | Mínimo 5 caracteres |
| department | string | Sim | Departamento | Mínimo 5 caracteres |
| phoneNumber | string | Sim | Telefone fixo | 10 dígitos (DDD + número) |
| telephoneNumber | string | Não | Celular | 11 dígitos (DDD + número) |
| email | string | Sim | E-mail institucional | Deve ser @saude.mg.gov.br |
| adress | string | Sim | Endereço | Mínimo 5 caracteres |

**Resposta de Sucesso (200)**

Retorna uma imagem PNG (binary data)

```
Content-Type: image/png
Content-Disposition: attachment; filename="assinatura.png"
```

**Erros Possíveis:**

**400 - Bad Request**
```json
{
  "success": false,
  "error": "Nenhum dado foi recebido",
  "status_code": 400
}
```

**422 - Validation Error**
```json
{
  "success": false,
  "error": "Erro de validação",
  "status_code": 422,
  "errors": {
    "fullName": "Nome deve conter apenas letras e espaços (mínimo 5 caracteres)",
    "email": "E-mail deve ser do domínio @saude.mg.gov.br",
    "phoneNumber": "Telefone deve ter 10 dígitos (DDD + número)"
  }
}
```

**500 - Internal Server Error**
```json
{
  "success": false,
  "error": "Erro interno do servidor. Por favor, contate o suporte.",
  "status_code": 500
}
```

**Exemplo cURL:**
```bash
curl -X POST http://localhost:5000/api/signature \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor de Software",
    "department": "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
    "phoneNumber": "3139160000",
    "telephoneNumber": "31987654321",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
  }' \
  --output assinatura.png
```

**Exemplo JavaScript (Fetch):**
```javascript
const data = {
  fullName: "João Pedro Silva",
  jobTitle: "Desenvolvedor de Software",
  department: "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
  phoneNumber: "3139160000",
  telephoneNumber: "31987654321",
  email: "joao.silva@saude.mg.gov.br",
  adress: "Cidade Administrativa, Prédio Minas, 1º andar"
};

fetch('http://localhost:5000/api/signature', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data),
})
  .then(response => response.blob())
  .then(blob => {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'assinatura.png';
    a.click();
  });
```

**Exemplo Python (Requests):**
```python
import requests

data = {
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor de Software",
    "department": "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
    "phoneNumber": "3139160000",
    "telephoneNumber": "31987654321",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
}

response = requests.post(
    'http://localhost:5000/api/signature',
    json=data
)

if response.status_code == 200:
    with open('assinatura.png', 'wb') as f:
        f.write(response.content)
```

---

### 3. Validar Dados

Valida os dados sem gerar a assinatura. Útil para validação em tempo real.

**Endpoint:** `POST /api/validate`

**Request Body:**

Mesma estrutura do endpoint `/api/signature`

**Resposta de Sucesso (200)**
```json
{
  "success": true,
  "message": "Dados validados com sucesso",
  "data": {
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor de Software",
    "department": "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
    "phoneNumber": "3139160000",
    "telephoneNumber": "31987654321",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
  }
}
```

**Erros Possíveis:**

Mesmos erros do endpoint `/api/signature`, exceto erros de geração de imagem.

**Exemplo cURL:**
```bash
curl -X POST http://localhost:5000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "João Pedro Silva",
    "jobTitle": "Desenvolvedor de Software",
    "department": "ASSESSORIA DE TECNOLOGIA DA INFORMAÇÃO",
    "phoneNumber": "3139160000",
    "email": "joao.silva@saude.mg.gov.br",
    "adress": "Cidade Administrativa, Prédio Minas, 1º andar"
  }'
```

---

## Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso |
| 400 | Requisição inválida |
| 404 | Recurso não encontrado |
| 405 | Método não permitido |
| 422 | Erro de validação |
| 500 | Erro interno do servidor |

## Regras de Validação

### Nome Completo (fullName)
- Mínimo 5 caracteres
- Apenas letras e espaços
- Regex: `^[A-Za-zÀ-ú\s]{5,}$`

### Cargo (jobTitle)
- Mínimo 5 caracteres
- Qualquer caractere
- Regex: `^.{5,}$`

### Departamento (department)
- Mínimo 5 caracteres
- Qualquer caractere
- Regex: `^.{5,}$`

### Telefone (phoneNumber)
- Exatamente 10 dígitos
- Formato: DDD + 8 dígitos
- Exemplo: `3139160000`
- Será formatado para: `(31) 3916-0000`

### Celular (telephoneNumber)
- Exatamente 11 dígitos (opcional)
- Formato: DDD + 9 dígitos
- Exemplo: `31987654321`
- Será formatado para: `(31) 98765-4321`

### E-mail (email)
- Deve ser do domínio @saude.mg.gov.br
- Regex: `^[a-zA-Z.]+@saude\.mg\.gov\.br$`
- Exemplo: `joao.silva@saude.mg.gov.br`

### Endereço (adress)
- Mínimo 5 caracteres
- Letras, números, pontos, vírgulas, hífens, barras
- Regex: `^[A-Za-zÀ-ú\s0-9.,º°\-\/\\]{5,}$`

## Normalização de Dados

Os dados são automaticamente normalizados antes da geração:

### Nome e Cargo
- Primeira letra de cada palavra em maiúscula
- Artigos e preposições em minúscula (de, da, do, e, em)
- Exemplo: `joão pedro da silva` → `João Pedro da Silva`

### Departamento
- Convertido para maiúsculas
- Exemplo: `assessoria de ti` → `ASSESSORIA DE TI`

### Telefones
- Formatados com parênteses e hífen
- Exemplo: `3139160000` → `(31) 3916-0000`

### E-mail
- Convertido para minúsculas
- Exemplo: `Joao.Silva@saude.mg.gov.br` → `joao.silva@saude.mg.gov.br`

### Endereço
- Primeira letra de cada palavra em maiúscula
- Siglas mantidas em maiúsculas (BH, MG, etc)
- Exemplo: `cidade administrativa, bh, mg` → `Cidade Administrativa, BH, MG`

## Rate Limiting

Atualmente não há rate limiting implementado. Em produção, recomenda-se:
- 100 requisições por minuto por IP
- Implementado via Nginx

## CORS

A API aceita requisições de:
- `http://localhost:5173` (desenvolvimento)
- `http://localhost:3000` (desenvolvimento)
- Configurável via variável de ambiente `CORS_ORIGINS`

## Logs

Todas as requisições são logadas com:
- Timestamp
- Método HTTP
- Endpoint
- Status code
- Tempo de resposta
- Erros (se houver)

## Versionamento

Versão atual: **2.0.0**

Futuras versões serão acessíveis via:
- `/api/v2/signature`
- `/api/v3/signature`

## Suporte

Para suporte ou reportar bugs:
- E-mail: suporte@saude.mg.gov.br
- Issues: GitHub repository

---

**Última atualização**: 2024
**Versão da API**: 2.0.0
