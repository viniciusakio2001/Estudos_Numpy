# %%
import numpy as np

# ============================================================================
# MÓDULO 8 — AGREGAÇÕES E ESTATÍSTICA
# ============================================================================
#
# O que é Agregação?
# ==================
# Agregação resume um array em um ÚNICO valor (ou menos dimensões).
#
# Exemplos:
# - sum: somar todos os elementos
# - mean: calcular a média de todos os elementos
# - max: encontrar o maior valor
# - std: desvio padrão (dispersão dos dados)
#
# Por que é importante?
# - Resumir dados para análise
# - Calcular métricas por sensor, período, categoria
# - Detectar anomalias (média ± desvio padrão)
# - Comparação entre grupos
#
# ============================================================================

print("\n=== 1. AGREGAÇÕES BÁSICAS — SUM E MEAN ===\n")

# Dados de consumo (kWh) de 3 máquinas em 5 dias
consumo = np.array([
    [120, 125, 130, 128, 132],  # máquina 1
    [95,  98,  102, 100, 105],  # máquina 2
    [180, 185, 190, 188, 195]   # máquina 3
])

print(f"Consumo (shape {consumo.shape}):\n{consumo}\n")

# PERGUNTA ANTES DE IMPLEMENTAR:
# - Qual é a soma TOTAL de consumo (todos os elementos)?
# - A soma total é: 2073
# - Qual é o consumo MÉDIO em geral?
# - O Consumo médio é: 
# Faça uma estimativa:

# TODO(human): Use np.sum() e np.mean() SEM especificar axis
soma_total = np.sum(consumo)
media_geral = np.mean(consumo)

print(f"Soma total de consumo: {soma_total} kWh\n")
print(f"Consumo médio geral: {media_geral:.2f} kWh\n")

# Pergunta: qual é o shape do resultado?
# Resposta: o shape é ()

print("=" * 60)

# %%
print("\n=== 2. AGREGAÇÕES POR EIXO — axis=0 vs axis=1 ===\n")

print(f"Consumo (shape {consumo.shape}):\n{consumo}\n")

# axis=0 → agregar ao LONGO das LINHAS (primira dimensão)
# Resultado: 1 valor por COLUNA (dia)
print(f"Consumo ao longo das linhas: \n (shape:{np.sum(consumo, axis=0).shape})\n {np.sum(consumo, axis=0)}\n")
# PERGUNTA: qual será o shape?
# Resposta: o shape será (5,)

# TODO(human): Calcule a soma de consumo POR DIA (eixo 0)
# Dica: axis=0 significa "elimine a dimensão das máquinas"
consumo_dia = np.sum(consumo, axis=0)
print(f"Soma de consumo por dia: \n{consumo_dia}\n")

# axis=1 → agregar ao LONGO das COLUNAS (segunda dimensão)
# Resultado: 1 valor por LINHA (máquina)

# PERGUNTA: qual será o shape?
# Resposta: O shape é de: (3,)

# TODO(human): Calcule a soma de consumo POR MÁQUINA (eixo 1)
# Dica: axis=1 significa "elimine a dimensão dos dias"
consumo_maquina = np.sum(consumo, axis=1)
print(f"Soma de consumo por máquina: (shape: {consumo_maquina.shape})\n {consumo_maquina} \n")

# Validação: soma das linhas DEVE IGUALAR soma das colunas

print("=" * 60)

# %%
print("\n=== 3. MÉDIA, MÍNIMO E MÁXIMO POR EIXO ===\n")

print(f"Consumo (shape {consumo.shape}):\n{consumo}\n")

# TODO(human): Calcule a média de consumo POR MÁQUINA
mediaconsumo_maquina = np.mean(consumo, axis=1)
print(f"Média de consumo por máquina: (Shape: {mediaconsumo_maquina.shape})\n {mediaconsumo_maquina} \n")

# TODO(human): Calcule o MÍNIMO de consumo POR DIA
minconsumo_dia = np.min(consumo, axis=0)
print(f"Minimo de consumo por dia: (shape: {minconsumo_dia.shape}) \n {minconsumo_dia} \n") 

# TODO(human): Calcule o MÁXIMO de consumo POR DIA
maxconsumo_dia = np.max(consumo, axis=0)
print(f"Máximo de consumo por dia: (shape: {maxconsumo_dia.shape}) \n {maxconsumo_dia} \n")

# Pergunta: qual máquina consome mais em média?
# A máquina que consome mais
# A máquina que consome mais é a tereceira maquina
# Dica: use np.argmax()

maquina_alta = np.argmax(mediaconsumo_maquina)
print(f"A Máquina que consme mais é o indice: {maquina_alta} \n")
print("=" * 60)

# %%
print("\n=== 4. KEEPDIMS — PRESERVAR DIMENSÕES ===\n")

print(f"Consumo original (shape {consumo.shape}):\n{consumo}\n")

# SEM keepdims: dimensão desaparece
media_sem = np.mean(consumo, axis=1)
print(f"Média sem keepdims:(shape: {media_sem.shape}) \n {media_sem}\n")
# COM keepdims=True: dimensão é mantida como 1
# TODO(human): Use keepdims=True em np.mean()

media_com = np.mean(consumo, axis=1, keepdims=True)
print(f"Média com keepdims: ({media_com.shape}) \n {media_com} \n")

# Por que isso é útil?
# Com keepdims, você pode fazer broadcasting novamente!
# TODO(human): Normalize subtraindo a média (use keepdims)

consumo_normalizado = consumo - media_com
print(f"Consumo normalizado: (shape: {consumo_normalizado.shape})\n {consumo_normalizado} \n")

# Validação: média deve ser 0 para cada máquina
nova_media = np.mean(consumo_normalizado, axis=1)
print(f"Nova média por Máquina: \n {nova_media} \n")
print("=" * 60)

# %%
print("\n=== 5. DESVIO PADRÃO E VARIÂNCIA ===\n")

print(f"Consumo (shape {consumo.shape}):\n{consumo}\n")

# Desvio padrão (std) — mede quanto os dados variam em torno da média
# Valores altos = dados muito dispersos
# Valores baixos = dados próximos da média

# TODO(human): Calcule o desvio padrão de consumo POR MÁQUINA
std_por_maquina = np.std(consumo, axis=1)
print(f"Desvio padrão de consumo por máquina:\n{std_por_maquina}\n")

# Variância (var) — é o quadrado do desvio padrão
# TODO(human): Calcule a variância de consumo POR MÁQUINA
var_por_maquina = np.var(consumo, axis=1)
print(f"Variância de consumo por máquina:\n{var_por_maquina}\n")

# Validação: var deve ser igual a std²
print(f"Verificação (std²): {std_por_maquina**2}\n")

# Pergunta: qual máquina tem consumo mais consistente (menor variação)?
# Resposta: a máquina que tem mais constância é a maquina 2

maquina_consistente = np.argmin(std_por_maquina)
print(f"Máquina com consumo mais consistente: máquina {maquina_consistente + 1} (std={std_por_maquina[maquina_consistente]:.2f})\n")

print("=" * 60)

# %%
print("\n=== 6. MEDIANA — VALOR DO MEIO ===\n")

# Mediana é o valor que divide os dados ao meio
# Se 5 valores: [90, 95, 100, 105, 110] → mediana = 100 (índice 2)
# Diferentes de MÉDIA!

dados_exemplo = np.array([10, 20, 100, 200, 500])  # valores bem dispersos
print(f"Dados exemplo: {dados_exemplo}\n")

media = np.mean(dados_exemplo)
mediana = np.median(dados_exemplo)
print(f"Média:   {media}\n")
print(f"Mediana: {mediana}\n")

# Pergunta: por que a mediana é diferente da média?
# Resposta: a mediana não é afetada por valores extremos (outliers)

# TODO(human): Calcule a mediana de consumo POR MÁQUINA
mediana_por_maquina = np.median(consumo, axis=1)
print(f"Mediana de consumo por máquina:\n{mediana_por_maquina}\n")

print("=" * 60)

# %%
print("\n=== 7. PERCENTIS E QUANTIS ===\n")

print(f"Consumo (shape {consumo.shape}):\n{consumo}\n")

# Percentil = valor abaixo do qual X% dos dados se encontram
# 25º percentil: 25% dos dados estão abaixo deste valor
# 50º percentil: mediana
# 75º percentil: 75% dos dados estão abaixo deste valor

# Exemplo: Q1, Q2 (mediana), Q3
consumo_flat = consumo.flatten()  # todos os 15 valores
print(f"Todos os valores (15 elementos):\n{np.sort(consumo_flat)}\n")

# TODO(human): Use np.percentile() para encontrar 25º, 50º, 75º percentis
p25 = np.percentile(consumo_flat, 25)
p50 = np.percentile(consumo_flat, 50)
p75 = np.percentile(consumo_flat, 75)

print(f"25º percentil (Q1): {p25}\n")
print(f"50º percentil (Q2/mediana): {p50}\n")
print(f"75º percentil (Q3): {p75}\n")

# IQR (Interquartile Range) — amplitude do intervalo central
iqr = p75 - p25
print(f"IQR (Q3 - Q1): {iqr}\n")

# Uso prático: detectar outliers
# Outlier = valor fora de [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
limite_inferior = p25 - 1.5 * iqr
limite_superior = p75 + 1.5 * iqr
print(f"Intervalo de outliers: [{limite_inferior:.2f}, {limite_superior:.2f}]\n")

outliers = consumo_flat[(consumo_flat < limite_inferior) | (consumo_flat > limite_superior)]
print(f"Valores considerados outliers: {outliers}\n")

print("=" * 60)

# %%
print("\n=== 8. CUMULATIVO — CUMSUM E CUMPROD ===\n")

# Cumulative Sum — cada posição é a soma até aquele ponto
dados_simples = np.array([10, 20, 30, 40])
print(f"Dados originais: {dados_simples}\n")

# TODO(human): Use np.cumsum() sem axis
cumsum_total = np.cumsum(dados_simples)
print(f"Cumsum (soma acumulada): {cumsum_total}\n")

# Interpretação: [10, 30, 60, 100]
# Posição 0: 10 (só o primeiro)
# Posição 1: 30 (10+20)
# Posição 2: 60 (10+20+30)
# Posição 3: 100 (10+20+30+40)

# Aplicação: consumo acumulado ao longo do mês
cumsum_por_dia = np.cumsum(consumo, axis=1)
print(f"Consumo acumulado por máquina:\n{cumsum_por_dia}\n")

# Pergunta: qual é o consumo acumulado total da máquina 1 até o dia 3?
# Resposta: cumsum_por_dia[0, 2] = 375

consumo_acumulado_m1_d3 = cumsum_por_dia[0, 2]
print(f"Consumo acumulado da máquina 1 até o dia 3: {consumo_acumulado_m1_d3} kWh\n")

print("=" * 60)

# %%
print("\n=== 9. DESAFIO — Análise Estatística Completa ===\n")

# Dataset: leituras de temperatura de 3 sensores em 6 horas
temperatura = np.array([
    [22.5, 23.1, 24.0, 23.5, 22.8, 23.2],  # sensor 1
    [20.5, 21.0, 21.5, 21.2, 20.8, 21.3],  # sensor 2
    [25.0, 25.5, 26.0, 25.8, 25.2, 25.9]   # sensor 3
])

print(f"Temperatura (shape {temperatura.shape}):\n{temperatura}\n")

# Passo 1: Calcular estatísticas por sensor
# TODO(human): Calcule: média, desvio padrão, mínimo, máximo POR SENSOR
media_temp = np.mean(temperatura, axis=1)
std_temp = np.std(temperatura, axis=1)
min_temp = np.min(temperatura, axis=1)
max_temp = np.max(temperatura, axis=1)

print(f"Média por sensor:     {media_temp}")
print(f"Desvio padrão:        {std_temp}")
print(f"Mínimo por sensor:    {min_temp}")
print(f"Máximo por sensor:    {max_temp}\n")

# Passo 2: Criar resumo de cada sensor
# TODO(human): Crie um array com a estrutura:
# [[media1, std1, min1, max1],
#  [media2, std2, min2, max2],
#  [media3, std3, min3, max3]]
# Dica: use reshape e stack, ou concatenate
resumo = np.column_stack([media_temp, std_temp, min_temp, max_temp])
print(f"Resumo por sensor (média, std, min, max):\n{resumo}\n")

# Passo 3: Qual sensor é mais estável (menor desvio)?
sensor_mais_estavel = np.argmin(std_temp)
print(f"Sensor mais estável: sensor {sensor_mais_estavel + 1} (desvio={std_temp[sensor_mais_estavel]:.3f})\n")

# Passo 4: Qual foi a hora de maior variação total?
# (suma do desvio de todos os sensores naquela hora)
variacao_por_hora = np.std(temperatura, axis=0)  # desvio entre sensores
hora_maior_variacao = np.argmax(variacao_por_hora)
print(f"Hora com maior variação entre sensores: hora {hora_maior_variacao} ({variacao_por_hora[hora_maior_variacao]:.3f})\n")

print("=" * 60)

# ============================================================================
# PRÓXIMOS PASSOS
# ============================================================================
# 1. Implemente todos os TODOs acima
# 2. Execute e estude os resultados
# 3. Explique por que sum(axis=0) + sum(axis=1) dão o mesmo resultado
# 4. Compare média vs mediana em dados com outliers
# 5. Use o desafio final para consolidar o Módulo 8

