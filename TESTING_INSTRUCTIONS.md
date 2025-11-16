# 🧪 Instruções de Teste - Gerador de Assinaturas

## ✅ Status Atual

### Backend
- ✅ **Rodando:** http://localhost:5000
- ✅ **Status:** Funcional e testado
- ✅ **Logs:** backend/logs/app.log

### Frontend
- ✅ **Rodando:** http://localhost:5173
- ✅ **Status:** Pronto para teste
- ✅ **Build:** Vite 6.4.1

---

## 🚀 Como Testar a Aplicação Completa

### 1. Acesse o Frontend
Abra seu navegador e acesse:
```
http://localhost:5173
```

### 2. Teste o Formulário

#### Dados de Teste Válidos
Use estes dados para testar:

```
Nome Completo: João Pedro Silva Santos
Cargo: Coordenador de Vigilância Epidemiológica
Departamento: COORDENADORIA DE VIGILÂNCIA EPIDEMIOLÓGICA
Telefone: (31) 3916-0000
Celular: (31) 98765-4321 (opcional)
E-mail: joao.silva@saude.mg.gov.br
Endereço: Cidade Administrativa, Prédio Minas, 1º andar
```

#### Passo a Passo
1. **Preencha todos os campos** com os dados acima
2. **Observe a validação** em tempo real
3. **Clique em "Gerar Assinatura"**
4. **Aguarde** a geração (1-2 segundos)
5. **Veja o preview** da assinatura gerada
6. **Clique em "Baixar Assinatura"** para salvar

### 3. Teste as Validações

#### Teste 1: Campo Vazio
1. Deixe um campo obrigatório vazio
2. Tente gerar a assinatura
3. **Esperado:** Mensagem de erro no campo

#### Teste 2: Formato Inválido
1. Digite um e-mail sem @saude.mg.gov.br
2. Tente gerar a assinatura
3. **Esperado:** Erro de validação

#### Teste 3: Telefone Inválido
1. Digite um telefone com menos dígitos
2. Tente gerar a assinatura
3. **Esperado:** Erro de formato

#### Teste 4: Formatação Automática
1. Digite um telefone sem formatação: 3139160000
2. **Esperado:** Formatação automática para (31) 3916-0000

### 4. Teste o Download

1. Gere uma assinatura válida
2. Clique em "Baixar Assinatura"
3. **Esperado:** Download de arquivo PNG
4. **Nome do arquivo:** assinatura_joao_pedro_silva_santos.png
5. **Tamanho:** ~150 KB
6. **Dimensões:** 800x641 pixels

### 5. Teste o Reset

1. Preencha o formulário
2. Clique em "Limpar"
3. Confirme a ação
4. **Esperado:** Todos os campos limpos

---

## 🔍 Verificações Visuais

### Layout
- ✅ Header com logo e título
- ✅ Formulário à esquerda
- ✅ Preview à direita
- ✅ Footer com informações
- ✅ Design responsivo

### Cores
- ✅ Roxo primário (#9333ea)
- ✅ Laranja secundário (#f97316)
- ✅ Verde sucesso (#16a34a)
- ✅ Vermelho erro (#dc2626)

### Interatividade
- ✅ Campos com focus visual
- ✅ Botões com hover effect
- ✅ Loading states
- ✅ Mensagens de erro/sucesso
- ✅ Animações suaves

---

## 🧪 Testes de API (Opcional)

### Teste 1: Health Check
```bash
curl http://localhost:5000/api/health
```
**Esperado:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-16T..."
}
```

### Teste 2: Validação
```bash
curl -X POST http://localhost:5000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "João Silva",
    "jobTitle": "Coordenador",
    "department": "VIGILÂNCIA",
    "phoneNumber": "(31) 3916-0000",
    "email": "joao@saude.mg.gov.br",
    "adress": "Cidade Administrativa"
  }'
```

### Teste 3: Geração
```bash
curl -X POST http://localhost:5000/api/signature \
  -H "Content-Type: application/json" \
  -d @backend/test_data.json \
  --output assinatura_teste.png
```

---

## 📱 Teste de Responsividade

### Desktop (> 1024px)
1. Abra em tela cheia
2. **Esperado:** Layout em 2 colunas

### Tablet (768px - 1024px)
1. Redimensione a janela
2. **Esperado:** Layout adaptado

### Mobile (< 768px)
1. Abra no celular ou redimensione
2. **Esperado:** Layout em coluna única

---

## ⚠️ Problemas Conhecidos

### Nenhum problema crítico identificado! ✅

Se encontrar algum problema:
1. Verifique os logs: `backend/logs/app.log`
2. Verifique o console do navegador (F12)
3. Verifique se ambos os servidores estão rodando

---

## 🐛 Troubleshooting

### Erro de CORS
**Problema:** Requisições bloqueadas

**Solução:**
1. Verifique se o backend está rodando
2. Verifique o arquivo `backend/.env`
3. CORS_ORIGINS deve incluir http://localhost:5173

### Erro 404
**Problema:** Endpoint não encontrado

**Solução:**
1. Verifique a URL da API no `frontend/.env`
2. Deve ser: `VITE_API_URL=http://localhost:5000`

### Imagem não carrega
**Problema:** Preview não aparece

**Solução:**
1. Verifique os logs do backend
2. Verifique se as fontes estão em `backend/static/fonts/`
3. Verifique se o template está em `backend/static/images/`

---

## ✅ Checklist de Teste

### Funcionalidades Básicas
- [ ] Formulário carrega corretamente
- [ ] Todos os campos são exibidos
- [ ] Validação funciona em tempo real
- [ ] Formatação automática de telefones
- [ ] Mensagens de erro aparecem
- [ ] Botão "Gerar" funciona
- [ ] Loading state aparece
- [ ] Preview da assinatura aparece
- [ ] Botão "Baixar" funciona
- [ ] Download da imagem funciona
- [ ] Botão "Limpar" funciona

### Validações
- [ ] Nome mínimo 5 caracteres
- [ ] Cargo mínimo 5 caracteres
- [ ] Departamento mínimo 5 caracteres
- [ ] Telefone formato correto
- [ ] Celular formato correto (opcional)
- [ ] E-mail @saude.mg.gov.br
- [ ] Endereço mínimo 5 caracteres

### UI/UX
- [ ] Design responsivo
- [ ] Cores corretas
- [ ] Fontes legíveis
- [ ] Botões com hover
- [ ] Focus visível
- [ ] Animações suaves
- [ ] Mensagens claras

### Performance
- [ ] Carregamento rápido (< 2s)
- [ ] Validação instantânea
- [ ] Geração rápida (< 2s)
- [ ] Download imediato

---

## 📊 Resultados Esperados

### Sucesso Total
- ✅ Todos os testes passam
- ✅ Nenhum erro no console
- ✅ Imagem gerada corretamente
- ✅ Download funciona
- ✅ UI responsiva

### Métricas
- **First Paint:** < 1s
- **Interactive:** < 2s
- **Validação:** < 100ms
- **Geração:** < 2s
- **Download:** Imediato

---

## 🎉 Conclusão

Se todos os testes passarem, o projeto está **100% funcional** e pronto para uso!

### Próximos Passos
1. ✅ Testar em diferentes navegadores
2. ✅ Testar em diferentes dispositivos
3. ✅ Coletar feedback dos usuários
4. ✅ Preparar para deploy em produção

---

**Boa sorte com os testes!** 🚀

Se encontrar qualquer problema, consulte:
- `backend/logs/app.log` - Logs do backend
- Console do navegador (F12) - Erros do frontend
- `FINAL_PROJECT_STATUS.md` - Status completo do projeto
