# %%
import numpy as np

# ============================================================================
# MÓDULO 7 — BROADCASTING
# ============================================================================
#
# O que é Broadcasting?
# ======================
# Broadcasting é o mecanismo que permite operações entre arrays de shapes
# DIFERENTES sem usar loops explícitos.
#
# Regra de Ouro:
# NumPy expande (implicitamente) o array menor para combinar com o maior,
# mas SEM copiar dados (eficiente em memória).
#
# Analogia:
# Se você faz: vetor (5,) + escalar (,) → NumPy "faz de conta" que o escalar
# é um array (5,) e soma elemento a elemento.
#
# ============================================================================

print("\n=== 1. BROADCASTING BÁSICO: ESCALAR ===\n")

# Exemplo: adicionar uma constante a todos os elementos
temperaturas = np.array([20.5, 21.3, 19.8, 25.1, 18.9])
print(f"Temperaturas originais (shape {temperaturas.shape}):\n{temperaturas}\n")

# Adicionar 5 graus (escalar) a cada temperatura
# TODO(human): Implemente a operação SEM usar loop:
temps_aumentadas = temperaturas + 5
print(f"Temperaturas + 5 (sua solução):\n{temps_aumentadas}\n")

# Pergunta: qual é o shape do resultado?
# Resposta:shape ainda será (5,)

# Por que não precisamos de loop? Porque NumPy faz broadcasting automático!
# O escalar (5) é "expandido" conceptualmente para (5,) para combinar.

# Pergunta: qual operação NumPy faz "por baixo"?
# (não é necessário responder agora, apenas pensar)

print("=" * 60)

# %%
print("\n=== 2. BROADCASTING 1D vs 1D (mesmo tamanho) ===\n")

# Sensores de temperatura (3 cidades)
temp_manha = np.array([18.0, 20.5, 19.3])
temp_noite = np.array([15.0, 17.3, 16.8])

print(f"Temperatura manhã (shape {temp_manha.shape}):\n{temp_manha}\n")
print(f"Temperatura noite (shape {temp_noite.shape}):\n{temp_noite}\n")

# Calcular diferença (apenas subtração, sem loop)
# TODO(human): Implemente a subtração:
diferenca = temp_manha - temp_noite
print(f"Diferença (sua solução, shape {diferenca.shape}):\n{diferenca}\n")

# Pergunta: qual é o shape do resultado? Por quê?
# Resposta: O Shape do resultado será (3,) não irá mudar

print("=" * 60)

# %%
print("\n=== 3. BROADCASTING 2D: Linha vs Coluna ===\n")

# Matriz de vendas por loja e dia
#       seg   ter   qua
# SP  [ 100   150   120 ]
# RJ  [ 200   180   210 ]
# MG  [  80   110    95 ]

vendas = np.array([
    [100, 150, 120],
    [200, 180, 210],
    [80,  110, 95]
])

print(f"Vendas (shape {vendas.shape}):\n{vendas}\n")

# Desconto por dia: 10% na terça, 5% na quarta, sem desconto segunda
desconto_percentual = np.array([0, 10, 5])
print(f"Desconto por dia % (shape {desconto_percentual.shape}):\n{desconto_percentual}\n")

# PERGUNTA ANTES DE IMPLEMENTAR:
# - Qual será o shape do resultado?
# - O shape do resultado vai ser (3,3)
# - Como NumPy vai alinhar desconto_percentual (3,) com vendas (3,3)?
# Responda: o broadcasting do numpy vai percorrer para cada coluna os descontos do array desconto percentual de acordo com as coluna do array de vendas

# Aplicar desconto (cada coluna recebe seu percentual)
# TODO(human): Realize a operação de subtração de desconto:
# Dica: vendas - (vendas * desconto_percentual / 100)
vendas_com_desconto = vendas - (vendas * desconto_percentual / 100)

print(f"Vendas com desconto (shape {vendas_com_desconto.shape}):\n{vendas_com_desconto}\n")

# Validação: quantos valores diferentes temos?
print(f"Número de valores únicos: {np.unique(vendas_com_desconto).size}\n")

print("=" * 60)

# %%
print("\n=== 4. AS REGRAS DE BROADCASTING ===\n")

# Regra 1: Se arrays têm número diferente de dimensões
#          → preenche com 1s à esquerda

# Regra 2: Compara shapes de trás para frente (direita)
#          → dimensões devem ser:
#            - iguais, OU
#            - uma delas é 1

# Regra 3: Dimensão de tamanho 1 é expandida para o outro tamanho

print("Exemplo de compatibilidade:\n")

# ✓ Compatível
shape_A = (3, 4)    # 3 linhas, 4 colunas
shape_B = (4,)      # 4 elementos → interpretado como (1, 4)
print(f"Shape A: {shape_A}")
print(f"Shape B: {shape_B}")
print(f"Após broadcast: (3, 4) ✓ compatível\n")

# ✓ Compatível
shape_C = (3, 1)    # 3 linhas, 1 coluna
shape_D = (3, 4)    # 3 linhas, 4 colunas
print(f"Shape C: {shape_C}")
print(f"Shape D: {shape_D}")
print(f"Após broadcast: (3, 4) ✓ compatível\n")

# ❌ INCOMPATÍVEL (veremos isso mais adiante)
shape_E = (3, 4)
shape_F = (2, 4)
print(f"Shape E: {shape_E}")
print(f"Shape F: {shape_F}")
print(f"Após broadcast: ??? ❌ ERRO — 3 ≠ 2\n")

print("=" * 60)

# %%
print("\n=== 5. EXERCÍCIO PRÁTICO: Normalizar Matriz ===\n")

# Dados de sensores (3 sensores × 4 medições)
dados = np.array([
    [10, 20, 15, 25],  # sensor 1
    [8,  18, 12, 22],  # sensor 2
    [12, 22, 18, 28]   # sensor 3
])

print(f"Dados brutos (shape {dados.shape}):\n{dados}\n")

# Calcular a MÉDIA de cada sensor (por linha)
# TODO(human): Use np.mean() com axis apropriado
# Dica: axis=1 para média por linha
media_por_sensor = np.mean(dados, axis=1)
print(f"Média por sensor (shape {media_por_sensor.shape}):\n{media_por_sensor}\n")

# PERGUNTA: qual será o shape de media_por_sensor?
# Resposta: o shape será de (3,)

# Normalizar: subtrair a média de cada sensor
# Desafio: media_por_sensor tem shape (3,), dados tem shape (3, 4)
# TODO(human): Como fazer essa subtração com broadcasting?
# Dica: você pode usar reshape() ou np.newaxis
# Tente esta versão:
media_reshape = media_por_sensor.reshape(-1, 1)
print(f"Média reformatada (shape {media_reshape.shape}):\n{media_reshape}\n")

# Agora subtraia:
# TODO(human): Implemente a normalização:
dados_normalizados = dados - media_reshape
print(f"Dados normalizados (shape {dados_normalizados.shape}):\n{dados_normalizados}\n")

# Validação: a média de cada linha deve ser ~0
print(f"Nova média por sensor:\n{np.mean(dados_normalizados, axis=1)}\n")

print("=" * 60)

# %%
print("\n=== 6. ALTERNATIVA: Usando np.newaxis ===\n")

# Em vez de reshape(), podemos usar np.newaxis (sintaxe idiomática)
# media_por_sensor[:, np.newaxis] expande (3,) → (3, 1)

media_newaxis = media_por_sensor[:, np.newaxis]
print(f"Média com newaxis (shape {media_newaxis.shape}):\n{media_newaxis}\n")

# TODO(human): Faça a mesma normalização usando newaxis:
dados_normalizados_v2 = dados - media_newaxis
print(f"Dados normalizados v2 (shape {dados_normalizados_v2.shape}):\n{dados_normalizados_v2}\n")

# São iguais?
print(f"Resultados idênticos? {np.array_equal(dados_normalizados, dados_normalizados_v2)}\n")

print("=" * 60)

# %%
print("\n=== 7. DESAFIO: Escalamento Min-Max com Broadcasting ===\n")

# Dados brutos de 3 sensores de pressão
pressao = np.array([
    [100, 105, 102, 108],  # sensor 1
    [98,  103, 100, 106],  # sensor 2
    [102, 107, 104, 110]   # sensor 3
])

print(f"Pressão bruta (shape {pressao.shape}):\n{pressao}\n")

# Escalamento Min-Max: (x - min) / (max - min)
# Objetivo: cada sensor tem valores entre 0 e 1

# Passo 1: encontrar min e max de cada sensor (por linha)
# TODO(human): Use np.min() e np.max() com axis=1
min_por_sensor = np.min(pressao, axis=1)
max_por_sensor = np.max(pressao, axis=1)

print(f"Min por sensor (shape {min_por_sensor.shape}):\n{min_por_sensor}\n")
print(f"Max por sensor (shape {max_por_sensor.shape}):\n{max_por_sensor}\n")

# Passo 2: Reformatar para broadcasting (shape (3,) → (3, 1))
# TODO(human): Use np.newaxis ou reshape():
min_reshape = min_por_sensor[:, np.newaxis]
max_reshape = max_por_sensor[:, np.newaxis]

print(f"Min reformatado (shape {min_reshape.shape}):\n{min_reshape}\n")

# Passo 3: Aplicar a fórmula
# TODO(human): Implemente a normalização min-max:
pressao_normalizada = (pressao - min_reshape) / (max_reshape - min_reshape)

print(f"Pressão normalizada (shape {pressao_normalizada.shape}):\n{pressao_normalizada}\n")

# Validação: cada sensor deve ter min=0 e max=1
print(f"Min normalizado: {np.min(pressao_normalizada, axis=1)}")
print(f"Max normalizado: {np.max(pressao_normalizada, axis=1)}\n")

print("=" * 60)

# %%
print("\n=== 8. TENTATIVA ERRADA: Broadcasting Incompatível ===\n")

# Este exemplo mostra o que NÃO funciona

arr_A = np.array([[1, 2, 3],
                   [4, 5, 6]])  # shape (2, 3)

arr_B = np.array([10, 20])     # shape (2,)

print(f"Array A (shape {arr_A.shape}):\n{arr_A}\n")
print(f"Array B (shape {arr_B.shape}):\n{arr_B}\n")

# PERGUNTA: o que acontece se tentar A + B?
# O NumPy vai tentar:
# 1. Alinhar shapes de trás para frente: (2, 3) vs (2,)
# 2. (2, 3) vs (1, 2) → interpretou como (1, 2) com newaxis
# 3. (2, 3) → 3 DEVE combinar com (1, 2) → não combina! 3 ≠ 2

# TODO(human): Tente executar esta linha (vai gerar erro):
# resultado = arr_A + arr_B
# print(resultado)

# Por que dá erro? Responda:
# A variavel resultado irá dar erro pq a quantidade de colunas é diferente da quantidade de colunas do shape B
# SOLUÇÃO: reformatar B para (2, 1) para que funcione
arr_B_reformatado = arr_B[:, np.newaxis]
print(f"Array B reformatado (shape {arr_B_reformatado.shape}):\n{arr_B_reformatado}\n")

# Agora funciona:
resultado = arr_A + arr_B_reformatado
print(f"A + B reformatado (shape {resultado.shape}):\n{resultado}\n")

print("=" * 60)

# ============================================================================
# PRÓXIMOS PASSOS
# ============================================================================
# 1. Implemente todos os TODOs acima e responda às perguntas
# implementei
# 2. Execute o código e verifique os resultados
# 3. Explique por que broadcasting funciona (comparar shapes)
# funciona para que não seja necessário realizar loop em python sendo mais performatico pelo numpy
# 4. Identifique qual operação NumPy faz "por baixo" (cópia vs view)
# acredito que ele utilize a cópia e faz essa referencia na mesma memória
