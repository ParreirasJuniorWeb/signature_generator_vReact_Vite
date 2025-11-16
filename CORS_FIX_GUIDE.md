# 🔧 Guia Rápido - Correção do CORS

## Problema Identificado
O frontend está rodando na porta **5174**, mas o backend só aceita requisições da porta **5173**.

## Solução

### Passo 1: Editar o arquivo .env do backend

1. Abra o arquivo: `backend/.env`

2. Encontre a linha:
```
CORS_ORIGINS=http://localhost:5173
```

3. Substitua por:
```
CORS_ORIGINS=http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174
```

4. Salve o arquivo (Ctrl+S)

### Passo 2: Reiniciar o Backend

1. No terminal do backend, pressione **Ctrl+C** para parar o servidor

2. Execute novamente:
```bash
cd backend
python run.py
```

3. Aguarde a mensagem:
```
* Running on http://127.0.0.1:5000
```

### Passo 3: Testar a Aplicação

1. Acesse: http://localhost:5174

2. Preencha o formulário com dados de teste:
```
Nome: João Pedro Silva
Cargo: Coordenador de Vigilância
Departamento: VIGILÂNCIA EPIDEMIOLÓGICA
Telefone: (31) 3916-0000
Celular: (31) 98765-4321
E-mail: joao.silva@saude.mg.gov.br
Endereço: Cidade Administrativa, Prédio Minas, 1º andar
```

3. Clique em **"Gerar Assinatura"**

4. **Resultado esperado:**
   - ✅ Loading aparece
   - ✅ Assinatura é gerada
   - ✅ Preview aparece
   - ✅ Botão de download funciona

## Verificação

Se ainda houver erro:

1. Abra o Console do navegador (F12)
2. Vá na aba "Network"
3. Tente gerar novamente
4. Verifique se há erros de CORS
5. Me informe o erro exato

## Arquivo de Referência

Criei o arquivo `backend/.env.example` com todas as configurações disponíveis para referência futura.

---

**Após seguir estes passos, a aplicação deve funcionar perfeitamente!** ✅
