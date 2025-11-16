# ✅ Checklist Completo de Testes - Gerador de Assinaturas

## 🎯 Testes Críticos (Opção C) - FAZER PRIMEIRO

### 1. Teste de Campo Inválido
- [x] Digite um e-mail sem @saude.mg.gov.br (ex: `joao@gmail.com`)
- [x] Tente gerar a assinatura
- [x] **Esperado:** Mensagem de erro aparece no campo
- [x] **Resultado:** Apareceu a mensagem de erro com um e-mail inválido (@gmail.com).

### 2. Teste de Download
- [x] Gere uma assinatura válida
- [x] Clique no botão "Baixar Assinatura"
- [x] **Esperado:** Arquivo PNG é baixado
- [x] **Nome do arquivo:** assinatura_[nome].png
- [x] **Tamanho:** ~150 KB
- [x] **Resultado:** Arquivo baixado corretamente com o nome e tamanho esperados.

### 3. Teste do Botão Limpar
- [x] Preencha todos os campos
- [x] Clique em "Limpar"
- [x] Confirme a ação
- [x] **Esperado:** Todos os campos ficam vazios
- [x] **Resultado:** Todos os campos foram limpos após a confirmação e clique do botão "Limpar".

---

## 📋 Testes Completos (Opção A)

### A. Validação de Campos Individuais

#### Campo: Nome Completo
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "João" (< 5 caracteres) → **Esperado:** Erro "Mínimo 5 caracteres"
- [x] Digite "João Pedro Silva" → **Esperado:** Sem erro
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: Cargo
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "Dev" (< 5 caracteres) → **Esperado:** Erro "Mínimo 5 caracteres"
- [x] Digite "Coordenador de TI" → **Esperado:** Sem erro
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: Departamento
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "TI" (< 5 caracteres) → **Esperado:** Erro "Mínimo 5 caracteres"
- [x] Digite "TECNOLOGIA DA INFORMAÇÃO" → **Esperado:** Sem erro
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: Telefone
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "31391600" (< 10 dígitos) → **Esperado:** Erro de formato
- [x] Digite "3139160000" → **Esperado:** Formata para (31) 3916-0000
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: Celular (Opcional)
- [x] Deixe vazio → **Esperado:** Sem erro (é opcional)
- [X] Digite "319876543" (< 11 dígitos) → **Esperado:** Erro de formato
- [x] Digite "31987654321" → **Esperado:** Formata para (31) 98765-4321
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: E-mail
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "joao@gmail.com" → **Esperado:** Erro "Deve ser @saude.mg.gov.br"
- [x] Digite "joao.silva@saude.mg.gov.br" → **Esperado:** Sem erro
- [x] **Resultado:** Campo validado corretamente conforme os critérios.

#### Campo: Endereço
- [x] Deixe vazio → **Esperado:** Erro "Campo obrigatório"
- [x] Digite "BH" (< 5 caracteres) → **Esperado:** Erro "Mínimo 5 caracteres"
- [x] Digite "Cidade Administrativa, Prédio Minas" → **Esperado:** Sem erro
- [X] **Resultado:** A opção de indicar o andar, como 12 º andar, apresenta problemas com o caracter "º", gerando erro de validação mesmo quando o campo está correto.

---

### B. Formatação Automática

#### Telefone Fixo
- [x] Digite: `3139160000`
- [x] **Esperado:** Formata para `(31) 3916-0000`
- [x] **Resultado:** Validação e formatação funcionaram corretamente.

#### Celular
- [x] Digite: `31987654321`
- [x] **Esperado:** Formata para `(31) 98765-4321`
- [x] **Resultado:** Validação e formatação funcionaram corretamente.

---

### C. Estados de Loading

#### Durante Geração
- [x] Preencha o formulário
- [x] Clique em "Gerar Assinatura"
- [x] **Esperado:** 
  - Botão mostra "Gerando..."
  - Spinner aparece
  - Botão fica desabilitado
- [x] **Resultado:** Funcionalidade de loading funcionou conforme esperado.

#### Após Geração
- [x] Aguarde a geração completar
- [x] **Esperado:**
  - Botão volta ao normal
  - Preview aparece
  - Mensagem de sucesso
- [x] **Resultado:** Funcionalidade de loading funcionou conforme esperado.
---

### D. Preview e Download

#### Qualidade da Imagem
- [x] Gere uma assinatura
- [x] Observe o preview
- [x] **Verificar:**
  - Texto legível
  - Cores corretas (roxo e laranja)
  - Sem distorções
  - Tamanho adequado
- [x] **Resultado:** Funcionalidade de loading funcionou conforme esperado.

#### Download
- [x] Clique em "Baixar Assinatura"
- [x] Verifique o arquivo baixado
- [x] **Verificar:**
  - Nome: `assinatura_[nome_completo].png`
  - Tamanho: ~150 KB
  - Dimensões: 800x641 pixels
  - Qualidade: Alta
- [x] **Resultado:** Funcionalidade de loading funcionou conforme esperado e dados da imagem corretos.

#### Múltiplas Gerações
- [x] Gere uma assinatura
- [x] Altere os dados
- [x] Gere novamente
- [x] Repita 3 vezes
- [x] **Esperado:** Todas funcionam sem erro
- [x] **Resultado:** Funcionou conforme esperado.

---

### E. Responsividade

#### Desktop (> 1024px)
- [x] Abra em tela cheia
- [x] **Verificar:**
  - Layout em 2 colunas
  - Formulário à esquerda
  - Preview à direita
  - Espaçamento adequado
- [x] **Resultado:** Funcional

#### Tablet (768px - 1024px)
- [x] Redimensione a janela para ~900px
- [x] **Verificar:**
  - Layout adaptado
  - Elementos visíveis
  - Sem scroll horizontal
- [x] **Resultado:** Funcional

#### Mobile (< 768px)
- [x] Redimensione para ~400px ou use DevTools
- [x] **Verificar:**
  - Layout em coluna única
  - Formulário acima
  - Preview abaixo
  - Botões acessíveis
- [x] **Resultado:** Funcional
---

### F. Casos de Erro

#### Campos Vazios
- [x] Deixe todos os campos vazios
- [x] Tente gerar
- [x] **Esperado:** Erros em todos os campos obrigatórios
- [x] **Resultado:** Funcional

#### E-mail Inválido
- [x] Digite: `joao@gmail.com`
- [x] Tente gerar
- [x] **Esperado:** Erro "Deve ser @saude.mg.gov.br"
- [x] **Resultado:** Funcional

#### Telefone Inválido
- [x] Digite: `319160000` (9 dígitos)
- [x] Tente gerar
- [x] **Esperado:** Erro de formato
- [x] **Resultado:** Funcional

#### Nome Muito Longo
- [x] Digite um nome com 100+ caracteres
- [x] Gere a assinatura
- [x] **Esperado:** 
  - Assinatura gerada
  - Texto ajustado (fonte menor)
  - Sem cortes
- [x] **Resultado:** Funcional

---

### G. Funcionalidades Gerais

#### Botão Limpar
- [x] Preencha todos os campos
- [x] Clique em "Limpar"
- [x] **Esperado:** Confirmação aparece
- [x] Confirme
- [x] **Esperado:** Todos os campos limpos
- [x] **Resultado:** Funcional

#### Navegação
- [x] Use Tab para navegar entre campos
- [x] **Esperado:** Focus visível em cada campo
- [x] **Resultado:** Funcional

#### Acessibilidade
- [x] Verifique se labels estão associados aos inputs
- [x] Teste navegação por teclado
- [x] **Esperado:** Totalmente acessível
- [x] **Resultado:** Funcional

---

## 📊 Resumo dos Resultados

### Testes Críticos (C)
- [x] Campo inválido: 2 erros encontrados e corrigidos
- [x] Download: Funcional
- [x] Botão limpar: Funcional

### Testes Completos (A)
- [x] Validação de campos: 7/7 passaram
- [x] Formatação automática: 2/2 passaram
- [x] Estados de loading: 2/2 passaram
- [x] Preview e download: 3/3 passaram
- [x] Responsividade: 3/3 passaram
- [x] Casos de erro: 4/4 passaram
- [x] Funcionalidades gerais: 3/3 passaram

### Total
- **Testes realizados:** 27/27
- **Testes passaram:** 24/27
- **Taxa de sucesso:** 90%

---

## 🐛 Bugs Encontrados

Liste aqui qualquer problema encontrado:

1. **Bug #1:**
   - Descrição: Campo de nome com apóstrofo (') não é aceito e textos meuito longos que NÃO se quebram na interface gráfica (texto com mais de 95 caracteres).
   - Como reproduzir: inserindo nomes com apóstrofo ou textos muito longos no campo de nome completo.
   - Severidade: [ ] Crítico [x] Alto [ ] Médio [ ] Baixo

2. **Bug #2:**
   - Descrição: Campo de endereço não aceita o caracter "º" (ex: 12 º andar).
   - Como reproduzir: inserindo o caracter "º" no campo de endereço.
   - Severidade: [ ] Crítico [ ] Alto [ ] Médio [x] Baixo

3. **Bug #3:**
   - Descrição: Problemas para gerar assinatura com nomes muito longos (mais de 95 caracteres) que não se quebram na interface gráfica.
   - Como reproduzir: inserindo nomes muito longos no campo de nome completo.
   - Severidade: [x] Crítico [ ] Alto [ ] Médio [ ] Baixo

---

## ✅ Conclusão

Após completar todos os testes, me informe:

1. **Quantos testes passaram?** 24/27
2. **Quantos bugs foram encontrados?** 4 (3 corrigidos, 1 pendente - Qualidade da imagem com nomes muito longos e quebra de linha)
3. **Bugs críticos?** [x] Sim [ ] Não
4. **Aplicação está pronta para uso?** [x] Sim [ ] Não

---

**Boa sorte com os testes!** 🚀

Quando terminar, me envie os resultados e eu corrijo qualquer bug encontrado!
