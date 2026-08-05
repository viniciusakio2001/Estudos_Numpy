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
