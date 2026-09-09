---
name: numpy-learning-progress
description: Rastreamento do progresso de aprendizado de NumPy
metadata: 
  node_type: memory
  type: project
  modified: 2026-07-27T00:00:00.000Z
---

## Módulos Completados

### ✓ Módulo 1 — Fundamentos de NumPy (COMPLETO)
- ✓ O que é NumPy: biblioteca para computação numérica vetorizada
- ✓ Quando utilizar: operações em grandes volumes, álgebra linear, simulações
- ✓ Importação padrão: `import numpy as np`
- ✓ **ndarray**: estrutura fundamental — arrays homogêneos
- ✓ Propriedades essenciais: `ndim`, `shape`, `size`, `dtype`, `itemsize`, `nbytes`
- ✓ Arrays 1D, 2D, 3D: criação e indexação
- ✓ Comparação listas Python vs arrays NumPy: velocidade e memória
- ✓ **Insight**: Arrays usam contiguidade de memória e operações vetorizadas (10-100x mais rápidos)

### ✓ Módulo 2 — Criação de arrays (COMPLETO)
- ✓ `np.zeros()` — arrays com zeros, inicialização de estruturas
- ✓ `np.ones()` — arrays com uns, base para multiplicação/scaling
- ✓ `np.arange()` — sequências com passo (tipo range, mas array)
- ✓ `np.linspace()` — N valores espaçados uniformemente (domínios matemáticos)
- ✓ `np.logspace()` — espaçamento logarítmico (frequências, dB, escalas exponenciais)
- ✓ `np.eye()` — matrizes identidade com parâmetro k para deslocamento
- ✓ `np.identity()` — matrizes identidade quadradas (restrição técnica vs eye)
- ✓ `np.diag()` — matrizes diagonais (aplicação: calibração de sensores)
- ✓ `np.full()` — arrays preenchidos com valor específico
- ✓ `np.empty()` — alocação rápida sem inicialização (use quando preencher 100%)
- ✓ `np.zeros_like()`, `np.ones_like()`, `np.full_like()` — baseadas em shape/dtype existente
- ✓ **Performance**: entendimento de custo e quando usar cada uma

### ✓ Módulo 3 — Tipos de dados (COMPLETO)
- ✓ **Inteiros com sinal**: int8, int16, int32, int64 (podem ser negativos)
- ✓ **Inteiros sem sinal**: uint8, uint16, uint32, uint64 (apenas positivos, 0-255 para uint8)
- ✓ **Ponto flutuante**: float32 (4 bytes, ~7 dígitos), float64 (8 bytes, ~15 dígitos, padrão)
- ✓ **Booleanos**: bool_ (ocupa 1 byte, não 1 bit)
- ✓ **Números complexos**: complex64, complex128
- ✓ **Conversão com `astype()`**: cria novo array, não modifica original, trunca decimais
- ✓ **Limites numéricos**: `np.iinfo()` para inteiros, `np.finfo()` para floats
- ✓ **Overflow e wraparound**: int8(127) + 1 = -128 (comportamento cíclico)
- ✓ **Promoção de tipos**: int + float = float; int + complex = complex
- ✓ **Economia de memória**: dtype adequado reduz RAM em Big Data
- ✓ **Insight**: Escolha de dtype impacta memória, velocidade e precisão — crítico em análise de dados

### ✓ Tópicos consolidados
- Diferenças entre operações em listas Python vs arrays NumPy
- Entendimento completo de dtype com arrays mistos
- Vetorização e velocidade de operações
- Broadcasting inicial (será aprofundado depois)

## Próximos Passos

### ⚪ Módulo 4 (Indexação e fatiamento) — PRÓXIMO
Essencial para extrair, modificar e filtrar dados:
- Índices positivos [0, 1, 2] e negativos [-1, -2, -3]
- Slicing com [start:stop:step]
- Arrays multidimensionais — indexação por linha/coluna
- Indexação booleana — filtros baseados em condições
- Indexação avançada com listas de índices
- Funções: `np.where()`, `np.nonzero()`, `np.argwhere()`
- **Prático**: Extrair valores de sensores acima de threshold

### ⚪ Módulo 5 (Alteração e organização)
Transformação de estrutura de arrays

### ⚪ Módulo 6 (Operações vetorizadas)
Substituir loops por operações elemento a elemento

### ⚪ Módulo 7 (Broadcasting)
Operações entre arrays de shapes diferentes

## Contexto de Aprendizado
- Foco em análise e manipulação de dados
- Dados de sensores como caso de uso prático
- Comparar loops Python vs vetorização
- Arquivo de estudos: `numpy_01.py`

## Histórico de Sessões

### Sessão Anterior — Módulo 1
- ✓ **O que é NumPy** — biblioteca para computação numérica vetorizada
- ✓ **Quando usar NumPy** — análise de dados, operações numéricas, álgebra linear
- ✓ **Instalação e importação** — `import numpy as np`, verificação de versão
- ✓ **ndarray** — estrutura fundamental de dados em NumPy (diferente de listas Python)
- ✓ **Diferenças listas vs arrays:**
  - Arrays são homogêneos (um dtype)
  - Listas Python são heterogêneas (múltiplos tipos)
  - Arrays NumPy são mais eficientes em memória e velocidade
- ✓ **Criação com `np.array()`** — conversão de listas para arrays
- ✓ **Arrays 1D, 2D, 3D** — estruturas unidimensionais, bidimensionais, multidimensionais
- ✓ **Propriedades essenciais:**
  - `ndim` — número de dimensões
  - `shape` — tamanho de cada dimensão (tupla)
  - `size` — total de elementos
  - `dtype` — tipo de dado dos elementos
  - `itemsize` — bytes por elemento
  - `nbytes` — total de bytes do array

#### Módulo 2 — Primeiras funções de criação (sessão anterior)
- ✓ `np.zeros()` — array com zeros
- ✓ `np.ones()` — array com uns
- ✓ `np.arange()` — sequência com passo (tipo range, mas NumPy)
- ✓ `np.linspace()` — divisão uniforme de intervalo

---

### Sessão 2026-07-27
- **Retomada dos estudos** após pausa
- Recapitulação do progresso (Módulo 1 completo, Módulo 2 parcial)

#### Aprendizados — Matrizes Identidade e Diagonais
- ✓ `np.eye()` — criação de matrizes identidade
  - Explicação: dtype float64 por padrão (necessário para álgebra linear)
  - Parâmetro `k` para deslocamento da diagonal
  - Diferença técnica com `np.identity()` (eye permite retangulares)
  
- ✓ `np.identity()` — matrizes identidade quadradas
  - Verificação: sem diferença visual, apenas restrição a matrizes quadradas
  
- ✓ `np.diag()` — matrizes com valores na diagonal
  - Aplicação prática: calibração de sensores
  - Uso em álgebra linear: `medicoes @ matriz_calibração`
  - Comparação: loop Python vs vetorização
  - Exercício: contagem de elementos (6 zeros em matriz 4×4)

#### Habilidades Desenvolvidas
- Compreensão de dtype e padrões NumPy
- Contagem de elementos em arrays
- Raciocínio sobre shapes e dimensões
- Aplicação prática em dados de sensores
- Diferença entre funções similares (eye vs identity vs diag)

#### Próxima Sessão
- Completar Módulo 2: `np.full()`, `np.empty()`, `np.logspace()`
- Depois: Módulo 3 (Tipos de dados)

---

### Sessão 2026-07-30
- **Retomada do Módulo 2** — completar funções restantes
- Arquivo de estudos: `numpy_10.py`

#### Aprendizados — Conclusão do Módulo 2
- ✓ `np.full()` — arrays preenchidos com valor específico
  - Uso prático: inicializar arrays com valores padrão (sensores "não medido")
  - Compreensão de dtype (float vs int)
  
- ✓ `np.empty()` — alocação sem inicialização
  - Mais rápido que `np.zeros()` quando vai preencher 100%
  - Risco: usar valores não inicializados
  - Caso prático: leitura de arquivos CSV
  
- ✓ `np.logspace()` — espaçamento logarítmico
  - Aplicação: frequências (Hz), dB, escalas que variam muito
  - Propriedade: espaçamento aumenta conforme cresce (não linear)
  - Exercício: teste de resposta de frequência (10 Hz a 10 kHz)
  
- ✓ `np.zeros_like()`, `np.ones_like()`, `np.full_like()`
  - Mantêm shape e dtype do array original
  - Vantagem: não precisa lembrar dimensões
  - Exercício: criar flags e estruturas para múltiplos sensores

#### Habilidades Desenvolvidas
- Entendimento completo de promoção de tipos (3.14 → float64)
- Cálculo de bytes em memória (elementos × 8 bytes)
- Análise de espaçamento em escalas logarítmicas
- Aplicação prática em sensores e monitoramento
- Consolidação do conceito de shape, dtype e nbytes

#### Observação
- Investigou uso de `datetime64` e `timedelta64` para timestamps
- Compreendeu que `astype()` será ensinado no Módulo 3
- Reconheceu a diferença entre timedelta64 (duração) vs datetime64 (data/hora)

#### Próxima Sessão
- Iniciar **Módulo 3 — Tipos de dados**
- Tópicos: int, float, bool, strings, complexos
- `astype()` para conversão
- `np.iinfo` e `np.finfo` (limites)
- Overflow e perda de precisão

---

### Sessão 2026-07-31
- **Início do Módulo 3 — Tipos de dados**

#### Aprendizados — Tipos numéricos e conversão
- ✓ **Tipos numéricos principais:**
  - `int8` (1 byte, -128 a 127) — economiza memória para valores pequenos
  - `int32` (4 bytes) — padrão em sistemas 32-bit
  - `int64` (8 bytes) — **padrão em NumPy**
  - `float32` (4 bytes) — menos preciso, mais rápido
  - `float64` (8 bytes) — **padrão em NumPy**
  - `bool` (1 byte) — True/False
  
- ✓ **Impacto de dtype em memória:**
  - Exemplo prático: 1 milhão de inteiros (0-100) em int8 vs int64 = economia de 7 MB
  - Escolha de dtype determina espaço ocupado
  
- ✓ **Operações aritméticas e tipos:**
  - Divisão `10 / 3` retorna float64 (resultado exato: 3.33333333)
  - Compreensão de promoção de tipos em operações
  
- ✓ **Conversão com `astype()`:**
  - `astype()` cria um **novo array**, não modifica o original
  - Truncagem de decimais: `3.7 → 3` (não arredonda)
  - Necessário atribuir a variável para manter o resultado
  - Quando usar: conversão de dados recebidos, não para redeclaração desnecessária
  
#### Habilidades Desenvolvidas
- Compreensão de tamanho de tipos e economia de memória
- Entendimento de quando usar cada dtype
- Noção clara sobre comportamento de astype() vs redeclaração
- Reconhecimento de truncagem vs arredondamento em conversões

#### Próximos Passos
- Exercício prático: conversão de temperaturas float → int
- `np.iinfo()` e `np.finfo()` (limites de tipos)
- Overflow e comportamento em limites
- Conversão para bool, strings, datetime64

---

### Sessão 2026-08-04
- **Conclusão do Módulo 3 — Tipos de dados** e revisão final dos Módulos 1-3
- Arquivos de estudos: `numpy_13.py`, `numpy_14.py`, `numpy_15.py`, `numpy_16.py`, `numpy_17.py`

#### Aprendizados — Complemento do Módulo 3
- ✓ **Tipos inteiros com e sem sinal:**
  - Com sinal: int8, int16, int32, int64 (podem ser negativos)
  - Sem sinal: uint8, uint16, uint32, uint64 (apenas positivos, 0 a 255 para uint8)
  - Aplicação: uint8 para imagens (0-255), astype(np.uint8) para conversão
  
- ✓ **Ponto flutuante e precisão:**
  - float32 (4 bytes, ~7 dígitos) — menor memória, menos preciso
  - float64 (8 bytes, ~15 dígitos) — **padrão em NumPy**, maior precisão
  - Aplicação: usar float32 em dados de sensores para economizar RAM
  
- ✓ **Booleanos:**
  - bool_ em NumPy ocupa 1 byte (não 1 bit como esperado)
  - Operações lógicas retornam bool_
  
- ✓ **Números complexos:**
  - complex64 (2 floats de 32 bits)
  - complex128 (2 floats de 64 bits)
  
- ✓ **Limites numéricos com `np.iinfo()` e `np.finfo()`:**
  - `np.iinfo(np.int8)`: min=-128, max=127, bits=8
  - `np.finfo(np.float32)`: min, max, eps (épsilon), precisão
  - Ferramenta para entender limites de cada tipo
  
- ✓ **Overflow e wraparound:**
  - int8(127) + 1 = -128 (comportamento cíclico, não erro)
  - Importante para detecção de anomalias em sensores
  
- ✓ **Promoção de tipos:**
  - int + float = float (resultado com mais precisão)
  - int + complex = complex
  - Automaticamente NumPy escolhe o tipo mais abrangente

#### Consolidação dos Módulos 1-3
- ✓ Diferenças fundamentais: listas Python são heterogêneas e lentas; arrays NumPy são homogêneos e rápidos
- ✓ Propriedades essenciais: ndim, shape, size, dtype, itemsize, nbytes
- ✓ Múltiplas formas de criar arrays: np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()
- ✓ Economia de memória através de escolha adequada de dtype
- ✓ Conversão segura entre tipos com astype()
- ✓ Compreensão de broadcasting inicial (será aprofundado no Módulo 7)

#### Habilidades Consolidadas
- Criação e configuração de arrays conforme necessidade
- Entendimento profundo de tipos de dados e impacto em memória
- Capacidade de diagnosticar problemas de tipo e espaço em memória
- Compreensão de vetorização vs loops Python
- Base sólida para operações e análise de dados

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (COMPLETO)
- ⚪ **Próximo** — Módulo 4: Indexação e fatiamento (essencial para manipulação de dados)

#### Próxima Sessão
- Iniciar **Módulo 4 — Indexação e fatiamento**
- Tópicos: índices positivos/negativos, slicing, arrays multidimensionais
- Indexação booleana para filtros
- Funções: `np.where()`, `np.nonzero()`, `np.argwhere()`
- Prático: extrair valores de sensores acima de threshold

---

### Sessão 2026-08-05
- **Consolidação dos Módulos 1-3** e **Preparação para Módulo 4**
- Arquivo de estudos: `numpy_17.py`

#### Aprendizados — Exercício Prático de Seleção de dtypes

**Contexto:** Revisão de exercício sobre escolha correta de dtypes para diferentes cenários reais

- ✓ **Seleção contextual de dtypes:**
  - IDs de usuários (0–10.000): `uint16` (0–65.535) ✓ — economia de memória vs int64
  - Temperaturas contínuas (-10 a 50°C): `float32` (4 bytes) ✓ — precisão suficiente
  - Contadores (até 1 milhão): `uint32` (0–4.294.967.295) ✓ — sem sinal pois contadores são sempre ≥ 0

- ✓ **Erro comum — API de `np.iinfo()` e `np.finfo()`:**
  - ❌ Errado: `np.iinfo(array_uint16)` — passa o array completo
  - ✓ Correto: `np.iinfo(np.uint16)` ou `np.iinfo(array_uint16.dtype)` — passa o tipo de dado
  - Insight: funções de introspexão de tipos recebem dtype, não arrays
  - Diagnóstico: erro de tipo (TypeError) quando passa array inteiro

- ✓ **Diferenciação entre `np.arange()` e `np.linspace()`:**
  - `np.arange(1, 11)`: sequência **incremental** (1, 2, 3, 4, 5...) — para contadores sequenciais
  - `np.linspace(1, 1000000, 10)`: distribuição **uniforme** (111111.11, 222222.22...) — para intervalos matemáticos
  - Contexto determina a função: contadores → arange; domínios matemáticos → linspace
  - Aprendizado: entender quando usar cada função baseado no caso de uso

#### Consolidação de Prática
- ✓ Criação de arrays com shapes apropriados
- ✓ Conversão com `.astype()` mantendo precisão
- ✓ Acesso a `shape`, `dtype`, `nbytes`
- ✓ Uso correto de `np.iinfo()` e `np.finfo()` para validar limites
- ✓ Cálculo de economia de memória (uint16 = 2 bytes vs int64 = 8 bytes)

#### Habilidades Consolidadas
- Escolha de dtype é **contextual** — requer conhecimento do domínio dos dados
- API NumPy distingue entre array e dtype em funções de introspecção
- Sequências vs distribuições são escolhas diferentes com impacto prático
- Capacidade de validar se um dtype é adequado usando `np.iinfo().max`

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (CONSOLIDADO E PRATICADO)
- ⚪ **Próximo** — Módulo 4: Indexação e fatiamento (começando na próxima sessão)

#### Preparação para Módulo 4
- **Contexto:** Indexação e fatiamento são essenciais para extrair, filtrar e modificar dados
- **Primeiros conceitos a praticar:**
  - Índices positivos [0, 1, 2...] e negativos [-1, -2...]
  - Slicing com [start:stop:step]
  - Exemplo inicial: `temperaturas = np.array([20.5, 21.3, 19.8, 25.1, 18.9, 22.4])`
    - Acessar primeira temperatura: `[0]`
    - Acessar última temperatura: `[-1]`
    - Acessar do índice 1 ao 3: `[1:4]`

---

### Sessão 2026-08-07
- **Consolidação Completa do Módulo 4 — Indexação e fatiamento**
- Arquivos de estudos: `numpy_18.py`, `numpy_20.py`

#### Aprendizados — Indexação e Fatiamento Completos

**Parte 1: Indexação 1D (numpy_18.py)**
- ✓ Indexação positiva: `arr[0]` — primeira posição
- ✓ Indexação negativa: `arr[-1]` — última posição
- ✓ Slicing com intervalo: `arr[2:6]` — índices 2 a 5
- ✓ Slicing a partir de um índice: `arr[5:]` — do índice 5 até o final
- ✓ Slicing inverso: `arr[::-1]` — inverte array com passo -1
- ✓ **100% de acertos** nos exercícios práticos

**Parte 2: Indexação 2D (numpy_20.py — exercícios prático-conceituais)**
- ✓ **Diferença crítica descoberta pelo usuário:**
  - `arr[1]` → shape (3,) — indexação simples REDUZ uma dimensão
  - `arr[1:2]` → shape (1, 3) — slicing PRESERVA todas as dimensões
  - Regra de ouro: slicing [start:stop] sempre preserva dimensões; indexação [n] reduz
  
- ✓ **Sintaxe 2D:**
  - Primeira dimensão (linha): `arr[linha]`
  - Segunda dimensão (coluna): `arr[:, coluna]`
  - Elemento específico: `arr[linha, coluna]` → retorna escalar (shape ())
  
- ✓ **Indexação booleana:**
  - Criação de máscara: `mascara = arr > 24.0` → shape igual ao array original
  - Aplicação de máscara: `arr[mascara]` → achata resultado para 1D
  - **Insight crítico:** máscara deve ser aplicada ao MESMO array em que foi criada

**Parte 3: Indexação Booleana com Múltiplas Condições**
- ✓ Combinação com operadores lógicos: `(arr >= 24) & (arr <= 25)`
- ✓ Sintaxe correta: parênteses em cada condição, operador `&` no meio
- ✓ Aplicação prática — Filtro de dados de sensores com múltiplos critérios

#### Erros Cometidos e Corrigidos
| Erro | Tipo | Diagnóstico |
|------|------|-----------|
| Usar índice 1 para hora 1 | Indexação 0-based | Primeiro = índice 0 |
| Shape (1,) para escalar | Dimensão | Testar com `.shape` |
| `arr >= 24 & <= 25` | Sintaxe | Usar parênteses: `(arr >= 24) & (arr <= 25)` |
| Aplicar máscara ao array errado | Lógica | Máscara deve vir do mesmo array |
| Contagem incorreta de valores | Validação manual | Tabular coluna por coluna |

#### Habilidades Desenvolvidas
- ✓ Indexação 1D e 2D completa
- ✓ Entendimento de redução vs preservação de dimensões
- ✓ Criação e aplicação de máscaras booleanas
- ✓ Combinação de múltiplas condições
- ✓ Validação manual de resultados

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (COMPLETO)
- ✅ **Módulo 4** — Indexação e fatiamento (COMPLETO E CONSOLIDADO)
- ⚪ **Próximo** — Módulo 5: Reshape, Transpose, Flatten

---

### Sessão 2026-08-20 — 2026-08-22
- **Consolidação Completa do Módulo 5 — Alteração e organização**
- Arquivos de estudos: `numpy_21.py`, `numpy_22.py`, `numpy_23.py`

#### Aprendizados — Manipulação de Dimensões

**Parte 1: reshape() e transpose()**
- ✓ `reshape()` — muda shape mantendo valores (view, não cópia)
- ✓ `transpose()` / `.T` — inverte linhas ↔ colunas (view, não cópia)
- ✓ Transposição em arrays não-contíguos requer cópia em `ravel()`

**Parte 2: flatten() vs ravel()**
- ✓ `flatten()` — **sempre copia**, seguro para modificações
- ✓ `ravel()` — **retorna view quando possível**, mais rápido
- ✓ Regra: use `flatten()` para segurança, `ravel()` para performance

**Parte 3: squeeze() e expand_dims()**
- ✓ `squeeze()` — remove **TODAS** dimensões de tamanho 1
- ✓ `squeeze(axis=n)` — remove **APENAS** a dimensão n se tiver tamanho 1
- ✓ `expand_dims(arr, axis=0)` — adiciona dimensão no início
- ✓ `expand_dims(arr, axis=1)` — adiciona dimensão no meio
- ✓ Visualização: axis=0 → formato horizontal (1, n); axis=1 → formato vertical (n, 1)

**Parte 4: newaxis — sintaxe alternativa**
- ✓ `arr[np.newaxis, :]` equivale a `expand_dims(arr, axis=0)`
- ✓ `arr[:, np.newaxis]` equivale a `expand_dims(arr, axis=1)`
- ✓ Vantagem: sintaxe compacta, idiomática em NumPy

**Parte 5: np.tile() — replicação de arrays**
- ✓ `np.tile(arr, (n_linhas, n_colunas))` — replica array
- ✓ Require 2D mínimo: precisa de `expand_dims()` antes se partindo de 1D

#### Desafio Final — Encadeamento de Operações
- ✓ Transformação (1,1,4) → (4,) com `squeeze()`
- ✓ Expansão (4,) → (1,4) com `expand_dims()`
- ✓ Replicação (1,4) → (10,4) com `np.tile()`
- ✓ Transposição (10,4) → (4,10) com `.T`

#### Erros Identificados e Corrigidos
| Erro | Tipo | Solução |
|------|------|---------|
| Usar array novo em passo 3 | Lógica | Continuar com resultado anterior |
| `print(shape)` ao invés de `print(shape.shape)` | Sintaxe | Usar `.shape` para acessar propriedade |

#### Habilidades Consolidadas
- ✓ Manipulação completa de dimensões (adicionar, remover, reorganizar)
- ✓ Compreensão de views vs cópias em operações de reshape
- ✓ Encadeamento eficiente de transformações
- ✓ Aplicação prática: preparar dados de sensores para análise

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (COMPLETO)
- ✅ **Módulo 4** — Indexação e fatiamento (COMPLETO)
- ✅ **Módulo 5** — Alteração e organização (COMPLETO)
- ⚪ **Próximo** — Módulo 6: Operações vetorizadas (começando próxima sessão)

---

### Sessão 2026-09-06
- **Consolidação Completa do Módulo 6 — Operações vetorizadas**
- Arquivos de estudos: `numpy_24.py`, `numpy_25.py`

#### Aprendizados — Operações Vetorizadas Completas

**Parte 1: Operações Aritméticas e Comparações (numpy_24.py)**
- ✓ Operações aritméticas vetorizadas (sem loops)
- ✓ Conversão de unidades: Celsius → Fahrenheit (F = C × 1.8 + 32)
- ✓ Criação de máscaras booleanas com comparadores
- ✓ Aplicação de máscaras para extração de dados
- ✓ Combinação de múltiplas condições com operadores lógicos (`&`, `|`)
- ✓ Operações in-place (`*=`, `+=`) para economizar RAM
- ✓ Funções matemáticas universais: `np.abs()`, `np.sqrt()`, `np.power()`

**Parte 2: Métodos de ufunc e Funções Matemáticas (numpy_25.py)**
- ✓ `np.add.reduce()` — agregação cumulativa final
- ✓ `np.add.accumulate()` — retorna todos os passos intermediários
- ✓ **Conceito crítico:** último valor de `accumulate()` = resultado de `reduce()`
- ✓ `np.multiply.outer()` — operação entre TODOS os pares
- ✓ Trigonometria: `np.sin()`, `np.cos()`, identidade sin² + cos² = 1
- ✓ Logaritmo e exponencial: `np.log()` como inverso de `np.exp()`
- ✓ `np.where()` — operação condicional vetorizada (IF-THEN-ELSE)
- ✓ Encadeamento de operações: conversão → normalização → logaritmo → classificação

**Parte 3: Benchmarking e Performance**
- ✓ Comparação prática: loop Python vs vetorização
- ✓ Dataset de 1 milhão de elementos: vetorização é **10-100x mais rápida**
- ✓ Validação com `np.array_equal()` para confirmar resultados

**Parte 4: Conceito de Discretização**
- ✓ `np.linspace(0, 2π, 8)` cria 8 pontos igualmente espaçados
- ✓ Resolução de amostragem afeta precisão
- ✓ Com 8 pontos: máximo do seno está em índice 2 (ângulo ≈ 1.80), não exatamente em π/2 (≈ 1.57)
- ✓ Diferença ≈ 0.22 radianos é esperada — trade-off entre resolução e quantidade de amostras
- ✓ Mais pontos = melhor resolução; menos pontos = aproximação grosseira

#### Erros Identificados e Corrigidos
| Erro | Tipo | Solução |
|------|------|---------|
| Typo: `np.log(an)` | Sintaxe | Corrigido: `np.log(crescimento_exp)` |
| Índice seno máximo = 8 | Indexação | Corrigido: índice 2 (valores 0-7 apenas) |
| Índice cosseno máximo = 8 | Indexação | Corrigido: índices 0 e 7 (máximo em π e 2π) |
| Não validar com `np.argmax()` | Prática | Adicionado: validação com impressão dos índices |
| accumulate() ≠ reduce() | Conceitual | Esclarecido: último elemento de accumulate = resultado de reduce |

#### Habilidades Consolidadas
- ✓ Substituição completa de loops por operações vetorizadas
- ✓ Entendimento profundo de ufuncs e seus métodos
- ✓ Composição de operações complexas em sequência
- ✓ Validação de resultados com funções auxiliares
- ✓ Benchmarking prático de performance
- ✓ Conceito fundamental: discretização e resolução de amostragem

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (COMPLETO)
- ✅ **Módulo 4** — Indexação e fatiamento (COMPLETO)
- ✅ **Módulo 5** — Alteração e organização (COMPLETO)
- ✅ **Módulo 6** — Operações vetorizadas (COMPLETO)
- ⚪ **Próximo** — Módulo 7: Broadcasting (começando próxima sessão)

---

### Sessão 2026-09-09
- **Consolidação Completa do Módulo 7 — Broadcasting**
- Arquivos de estudos: `numpy_26.py`, `numpy_27.py`

#### Aprendizados — Broadcasting Completo

**Parte 1: Broadcasting Básico (numpy_26.py)**
- ✓ Broadcasting escalar: `array + 5` → expande escalar para (5,)
- ✓ Broadcasting 1D vs 1D: `(3,) - (3,)` → operação elemento a elemento
- ✓ Broadcasting 2D × 1D: `(3, 3) - (3,)` → desconto por coluna
  - **Conceito crítico:** desconto (3,) se aplica a CADA linha de vendas (3, 3)
  - Sem reshape, NumPy tenta alinhar da direita e falha (3 ≠ 3 em colunas)

**Parte 2: As 3 Regras de Broadcasting**
- ✓ **Regra 1:** Se arrays têm números diferentes de dimensões → preenche com 1s à esquerda
- ✓ **Regra 2:** Compara shapes da direita para esquerda → dimensões devem ser iguais OU uma é 1
- ✓ **Regra 3:** Dimensão de tamanho 1 é expandida para o outro tamanho
- ✓ **Aplicação crítica:** Quando `(3,)` alinha com `(3, 4)`:
  - (3,) interpretado como (1, 3) após Regra 1
  - (1, 3) vs (3, 4): incompatível → precisa reshape!
  - (3, 1) vs (3, 4): compatível → expande coluna

**Parte 3: reshape() vs np.newaxis — Duas Sintaxes Equivalentes**
- ✓ `media.reshape(-1, 1)` → (3,) → (3, 1) explícito
- ✓ `media[:, np.newaxis]` → (3,) → (3, 1) idiomático
- ✓ Ambas funcionam; segunda é mais Pythônica em NumPy

**Parte 4: Normalização Min-Max com Broadcasting (numpy_27.py)**
- ✓ Fórmula: `(valores - min) / (max - min)` → escala entre 0 e 1
- ✓ Cada sensor tem mín e máx diferentes (ex: sensor1: 20-24, sensor2: 19-23)
- ✓ Broadcasting expande (3, 1) para (3, 4) → normaliza cada linha proporcional
- ✓ Resultado: todas as linhas têm padrão igual [0.0, 0.5, 0.25, 0.75, 1.0]
  - Porque cada linha é normalizada pelo seu próprio intervalo
- ✓ Validação: mín normalizado = 0, máx normalizado = 1 ✓

#### Conceito Fundamental Consolidado

**Broadcasting NÃO duplica dados em memória** — é uma operação lógica que NumPy otimiza:
- (3, 1) permanece (3, 1), mas a operação com (3, 4) a trata como (3, 4)
- Economiza RAM em grandes datasets
- Operações vetorizadas: 10-100x mais rápidas que loops Python

#### Erros Identificados e Corrigidos
| Erro | Tipo | Solução |
|------|------|---------|
| Tentar `(3, 4) - (3,)` | Broadcasting | Reshape para (3, 1) com `reshape(-1, 1)` ou `[:, np.newaxis]` |
| Confundir `(3,)` com `(1, 3)` | Dimensão | NumPy alinha de trás para frente; usar `reshape()` para clareza |
| Pensar que broadcasting copia | Memória | NumPy apenas aplica lógica; sem duplicação |

#### Habilidades Consolidadas
- ✓ Compreensão profunda de como NumPy alinha shapes
- ✓ Aplicação prática em normalização de dados (min-max)
- ✓ Uso fluente de `reshape()` e `np.newaxis`
- ✓ Validação de compatibilidade de shapes antes de operações
- ✓ Reconhecimento de quando broadcast vai falhar

#### Status do Aprendizado
- ✅ **Módulo 1** — Fundamentos (COMPLETO)
- ✅ **Módulo 2** — Criação de arrays (COMPLETO)
- ✅ **Módulo 3** — Tipos de dados (COMPLETO)
- ✅ **Módulo 4** — Indexação e fatiamento (COMPLETO)
- ✅ **Módulo 5** — Alteração e organização (COMPLETO)
- ✅ **Módulo 6** — Operações vetorizadas (COMPLETO)
- ✅ **Módulo 7** — Broadcasting (COMPLETO E CONSOLIDADO)
- ⚪ **Próximo** — Módulo 8: Agregações e Estatística (começando próxima sessão)

#### Próxima Sessão
- Iniciar **Módulo 8 — Agregações e Estatística**
- Funções: `sum`, `mean`, `median`, `min`, `max`
- Agregações por eixo (`axis=0`, `axis=1`)
- Estatística: `std`, `var`, `percentile`, `quantile`
- `keepdims=True` para manter dimensões
- Aplicação prática: análise de dados de sensores
