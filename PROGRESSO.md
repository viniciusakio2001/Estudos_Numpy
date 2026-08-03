---
name: numpy-learning-progress
description: Rastreamento do progresso de aprendizado de NumPy
metadata: 
  node_type: memory
  type: project
  modified: 2026-07-27T00:00:00.000Z
---

## Módulos Completados

### ✓ Módulo 1 — Fundamentos de NumPy
- O que é NumPy e quando utilizá-lo
- Importação e versão
- Criação com `np.array()` a partir de listas
- Arrays 1D, 2D e 3D (já testou)
- Propriedades: `ndim`, `shape`, `size`, `dtype`

### ✓ Módulo 2 — Criação de arrays (COMPLETO)
- `np.zeros()` ✓
- `np.ones()` ✓
- `np.arange()` ✓
- `np.linspace()` ✓
- `np.eye()` ✓ (matrizes identidade, parâmetro k para deslocamento)
- `np.identity()` ✓ (diferença técnica: sempre quadrada)
- `np.diag()` ✓ (matrizes diagonais, aplicações em calibração de sensores)
- `np.full()` ✓ (arrays preenchidos com valor específico)
- `np.empty()` ✓ (alocação sem inicialização, uso quando preencher 100%)
- `np.logspace()` ✓ (espaçamento logarítmico, aplicações em frequências e escalas)
- `np.zeros_like()`, `np.ones_like()`, `np.full_like()` ✓ (criação baseada em outros arrays)

### ✓ Tópicos iniciais de comparação
- Diferenças entre operações em listas Python vs arrays NumPy
- Entendimento de `dtype` com arrays mistos

## Próximos Passos

### A fazer — Completar Módulo 2
- `np.full()` (Arrays com valor específico)
- `np.empty()` (Arrays não inicializados)
- `np.logspace()` (Espaçamento logarítmico)
- Criação baseada em outros arrays (`np.zeros_like`, `np.ones_like`, `np.full_like`)
- Definição explícita de tipos em funções de criação

### A fazer — Módulo 3 (Tipos de dados)
Explorar:
- Inteiros, ponto flutuante, booleanos
- Conversão com `astype()`
- `np.iinfo` e `np.finfo`

### A fazer — Módulo 4 (Indexação e fatiamento)
Essencial para manipulação de dados

### A fazer — Módulo 6 (Operações vetorizadas)
Essencial antes de Módulo 7

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
