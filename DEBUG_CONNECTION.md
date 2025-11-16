# 🔍 Diagnóstico de Conexão

## Problema Atual
"Erro de conexão. Verifique sua internet e tente novamente."

## Possíveis Causas

### 1. Backend não está rodando
**Verificar:**
- Abra http://localhost:5000/api/health no navegador
- **Esperado:** `{"status": "healthy", "timestamp": "..."}`
- **Se der erro:** Backend não está rodando

### 2. URL incorreta no frontend
**Verificar:**
- Abra o Console do navegador (F12)
- Vá na aba "Network"
- Tente gerar a assinatura
- Veja qual URL está sendo chamada
- **Deve ser:** `http://localhost:5000/api/signature`

### 3. CORS ainda bloqueando
**Verificar:**
- No Console (F12), procure por erros de CORS
- **Erro típico:** "Access to fetch at 'http://localhost:5000/api/signature' from origin 'http://localhost:5174' has been blocked by CORS policy"

### 4. Múltiplas instâncias do Vite
**Problema identificado:** Há várias instâncias do Vite rodando!

## Solução Passo a Passo

### Passo 1: Matar todos os processos Node
```bash
# Windows PowerShell
taskkill /F /IM node.exe

# Ou feche todos os terminais do VSCode
```

### Passo 2: Verificar se o backend está rodando
```bash
# Teste no navegador ou PowerShell
curl http://localhost:5000/api/health
```

**Se não estiver rodando:**
```bash
cd backend
python run.py
```

### Passo 3: Iniciar apenas UMA instância do frontend
```bash
cd frontend
npm run dev
```

### Passo 4: Testar a conexão

1. Abra: http://localhost:5174 (ou a porta que aparecer)

2. Abra o Console do navegador (F12)

3. Vá na aba "Network"

4. Tente gerar uma assinatura

5. **Observe:**
   - Qual requisição foi feita?
   - Qual foi o status code? (200, 404, 500, etc)
   - Há erros de CORS?
   - Há erros de rede?

## Teste Manual da API

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
curl -X POST http://localhost:5000/api/validate ^
  -H "Content-Type: application/json" ^
  -d "{\"fullName\":\"João Silva\",\"jobTitle\":\"Coordenador\",\"department\":\"VIGILÂNCIA\",\"phoneNumber\":\"(31) 3916-0000\",\"email\":\"joao@saude.mg.gov.br\",\"adress\":\"Cidade Administrativa\"}"
```

### Teste 3: Geração (via navegador)
Abra no navegador:
```
http://localhost:5000/api/health
```

## Informações Necessárias

Por favor, me informe:

1. **Backend está rodando?**
   - [ ] Sim, em http://localhost:5000
   - [ ] Não

2. **Quantos terminais estão abertos?**
   - Número: ___

3. **Console do navegador mostra:**
   - [ ] Erro de CORS
   - [ ] Erro 404
   - [ ] Erro 500
   - [ ] Erro de rede (ERR_CONNECTION_REFUSED)
   - [ ] Outro: ___________

4. **URL que o frontend está tentando acessar:**
   - (copie da aba Network do console)

5. **Porta do frontend:**
   - [ ] 5173
   - [ ] 5174
   - [ ] Outra: ___

---

**Com essas informações, posso identificar exatamente o problema!** 🔍
