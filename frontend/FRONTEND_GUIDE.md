# Guia do Frontend - Gerador de Assinaturas

## 📋 Visão Geral

Este é o frontend React do sistema de geração de assinaturas de e-mail da SES-MG. Construído com React 18, Vite e Tailwind CSS, oferece uma interface moderna e responsiva.

## 🏗️ Arquitetura

### Camadas da Aplicação

```
┌─────────────────────────────────────┐
│         Componentes (UI)            │
│  - SignatureForm                    │
│  - SignaturePreview                 │
│  - InputField, Button               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│      Custom Hooks (Lógica)          │
│  - useSignatureForm                 │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│    Serviços (Comunicação)           │
│  - ApiService                       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│    Utilitários (Helpers)            │
│  - Validators                       │
│  - Formatters                       │
└─────────────────────────────────────┘
```

## 🎯 Funcionalidades

### 1. Formulário de Dados
- ✅ Validação em tempo real
- ✅ Formatação automática (telefones)
- ✅ Mensagens de erro contextuais
- ✅ Campos obrigatórios e opcionais
- ✅ Feedback visual de erros

### 2. Preview da Assinatura
- ✅ Visualização em tempo real
- ✅ Loading state durante geração
- ✅ Download da imagem gerada
- ✅ Mensagens de sucesso/erro

### 3. Validações
- ✅ Nome completo (mínimo 5 caracteres)
- ✅ Cargo (mínimo 5 caracteres)
- ✅ Departamento (mínimo 5 caracteres)
- ✅ Telefone fixo (formato: (XX) XXXX-XXXX)
- ✅ Celular opcional (formato: (XX) XXXXX-XXXX)
- ✅ E-mail (@saude.mg.gov.br)
- ✅ Endereço (mínimo 5 caracteres)

## 📦 Componentes

### InputField
**Propósito:** Campo de entrada reutilizável com validação

**Props:**
- `label` (string): Rótulo do campo
- `name` (string): Nome do campo
- `value` (string): Valor atual
- `onChange` (function): Callback de mudança
- `onBlur` (function): Callback de blur
- `error` (string): Mensagem de erro
- `required` (boolean): Se é obrigatório
- `disabled` (boolean): Se está desabilitado

**Exemplo:**
```jsx
<InputField
  label="Nome Completo"
  name="fullName"
  value={formData.fullName}
  onChange={handleChange}
  error={errors.fullName}
  required
/>
```

### Button
**Propósito:** Botão reutilizável com variantes

**Props:**
- `variant` (string): primary, secondary, success, danger, outline
- `size` (string): sm, md, lg
- `loading` (boolean): Estado de carregamento
- `disabled` (boolean): Se está desabilitado
- `icon` (ReactNode): Ícone opcional

**Exemplo:**
```jsx
<Button
  variant="primary"
  size="lg"
  loading={isLoading}
  onClick={handleSubmit}
>
  Gerar Assinatura
</Button>
```

### SignatureForm
**Propósito:** Formulário completo de dados

**Props:**
- `formData` (object): Dados do formulário
- `errors` (object): Erros de validação
- `isLoading` (boolean): Estado de carregamento
- `onFieldChange` (function): Callback de mudança
- `onFieldBlur` (function): Callback de blur
- `onSubmit` (function): Callback de submit
- `onReset` (function): Callback de reset

### SignaturePreview
**Propósito:** Preview e download da assinatura

**Props:**
- `signatureUrl` (string): URL da imagem
- `isSuccess` (boolean): Se foi gerada com sucesso
- `isLoading` (boolean): Estado de carregamento
- `onDownload` (function): Callback de download

## 🔧 Custom Hooks

### useSignatureForm
**Propósito:** Gerencia todo o estado e lógica do formulário

**Retorna:**
```javascript
{
  // Estado
  formData,           // Dados do formulário
  errors,             // Erros de validação
  isLoading,          // Estado de carregamento
  signatureUrl,       // URL da assinatura gerada
  signatureBlob,      // Blob da imagem
  isSuccess,          // Se foi gerado com sucesso
  
  // Ações
  updateField,        // Atualiza um campo
  validateSingleField, // Valida um campo
  resetForm,          // Reseta o formulário
  generateSignature,  // Gera a assinatura
  downloadSignature,  // Faz download
  validateOnly,       // Valida sem gerar
}
```

**Exemplo de uso:**
```jsx
function MyComponent() {
  const {
    formData,
    errors,
    isLoading,
    updateField,
    generateSignature,
  } = useSignatureForm();

  const handleSubmit = async () => {
    const result = await generateSignature();
    if (result.success) {
      console.log('Assinatura gerada!');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* campos do formulário */}
    </form>
  );
}
```

## 🛠️ Utilitários

### Validators (validators.js)

**validateField(fieldName, value, isRequired)**
Valida um campo individual

**validateForm(formData)**
Valida todos os campos do formulário

**clearFieldError(errors, fieldName)**
Remove erro de um campo específico

### Formatters (formatters.js)

**formatPhone(value)**
Formata telefone fixo: (XX) XXXX-XXXX

**formatTelephone(value)**
Formata celular: (XX) XXXXX-XXXX

**formatName(value)**
Capitaliza nome corretamente

**formatDepartment(value)**
Converte para maiúsculas

**formatAddress(value)**
Formata endereço com siglas

**downloadBlob(blob, filename)**
Faz download de um blob

**blobToUrl(blob)**
Converte blob em URL

## 🌐 Serviços

### ApiService (api.service.js)

**healthCheck()**
Verifica status da API

**validateData(userData)**
Valida dados sem gerar assinatura

**generateSignature(userData)**
Gera a assinatura (retorna Blob)

**Exemplo:**
```javascript
import ApiService from './services/api.service';

// Gerar assinatura
const blob = await ApiService.generateSignature({
  fullName: 'João Silva',
  jobTitle: 'Coordenador',
  // ... outros campos
});

// Validar dados
const result = await ApiService.validateData(userData);
```

## 🎨 Estilos

### Tailwind CSS
O projeto usa Tailwind CSS para estilização. Classes principais:

**Cores:**
- `bg-purple-600` - Cor primária
- `bg-orange-500` - Cor secundária
- `bg-green-600` - Sucesso
- `bg-red-600` - Erro

**Espaçamento:**
- `p-4`, `p-6`, `p-8` - Padding
- `m-4`, `m-6`, `m-8` - Margin
- `space-y-4` - Espaçamento vertical

**Responsividade:**
- `md:` - Tablet (768px+)
- `lg:` - Desktop (1024px+)

## 🔄 Fluxo de Dados

```
1. Usuário preenche formulário
   ↓
2. Validação em tempo real (onChange)
   ↓
3. Validação completa (onBlur)
   ↓
4. Submit do formulário
   ↓
5. Validação final (validateForm)
   ↓
6. Requisição à API (ApiService)
   ↓
7. Recebe Blob da imagem
   ↓
8. Converte para URL (blobToUrl)
   ↓
9. Exibe preview
   ↓
10. Usuário faz download
```

## 🚀 Como Executar

### Desenvolvimento
```bash
npm run dev
```
Acesse: http://localhost:5173

### Build de Produção
```bash
npm run build
```
Arquivos gerados em: `dist/`

### Preview do Build
```bash
npm run preview
```

## 🧪 Testes

### Executar Testes
```bash
npm run test
```

### Interface de Testes
```bash
npm run test:ui
```

### Cobertura
```bash
npm run test:coverage
```

## 📱 Responsividade

O frontend é totalmente responsivo:

- **Mobile** (< 768px): Layout em coluna única
- **Tablet** (768px - 1024px): Layout adaptado
- **Desktop** (> 1024px): Layout em duas colunas

## ♿ Acessibilidade

- ✅ Labels associados aos inputs
- ✅ Mensagens de erro descritivas
- ✅ Focus visible
- ✅ Navegação por teclado
- ✅ ARIA labels onde necessário

## 🔒 Segurança

- ✅ Validação client-side
- ✅ Sanitização de inputs
- ✅ CORS configurado
- ✅ Sem dados sensíveis no código

## 📊 Performance

- ✅ Code splitting automático (Vite)
- ✅ Lazy loading de componentes
- ✅ Otimização de imagens
- ✅ Minificação de assets

## 🐛 Troubleshooting

### Erro de CORS
**Problema:** Requisições bloqueadas por CORS

**Solução:** Verifique se o backend está com CORS configurado:
```python
# backend/app/__init__.py
CORS(app, origins=['http://localhost:5173'])
```

### Erro de conexão
**Problema:** Não consegue conectar à API

**Solução:** Verifique se:
1. Backend está rodando (http://localhost:5000)
2. `.env` está configurado corretamente
3. Firewall não está bloqueando

### Erro de build
**Problema:** Build falha

**Solução:**
```bash
# Limpe cache e reinstale
rm -rf node_modules package-lock.json
npm install
npm run build
```

## 📚 Recursos Adicionais

- [React Docs](https://react.dev/)
- [Vite Docs](https://vitejs.dev/)
- [Tailwind CSS Docs](https://tailwindcss.com/)
- [Axios Docs](https://axios-http.com/)

## 👥 Contribuindo

1. Crie uma branch para sua feature
2. Faça commit das mudanças
3. Abra um Pull Request
4. Aguarde revisão

## 📄 Licença

ISC License - Secretaria de Estado de Saúde de Minas Gerais
