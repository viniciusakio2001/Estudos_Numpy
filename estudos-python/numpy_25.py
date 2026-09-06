# %%
import numpy as np
import time

# ============================================================================
# MÓDULO 6 — OPERAÇÕES VETORIZADAS (PARTE AVANÇADA)
# ============================================================================
#
# Tópicos:
# 1. Encadeamento de operações (composição)
# 2. Métodos de ufunc: reduce(), accumulate(), outer()
# 3. Funções matemáticas: sin, cos, log, exp
# 4. Operações condicionais: np.where()
# 5. Benchmark: loop vs vetorização real
#
# ============================================================================

print("\n=== 1. ENCADEAMENTO DE OPERAÇÕES ===\n")

# Dados brutos de sensores de temperatura
temp_celsius = np.array([20.5, 21.3, 19.8, 25.1, 18.9, 22.4])
print(f"Temperaturas (°C):\n{temp_celsius}\n")

# Tarefa: Converter para Fahrenheit, depois normalizar entre 0-1
# Fórmula:
#   1. F = C * 1.8 + 32
#   2. Normalizar: (F - min(F)) / (max(F) - min(F))

# Você pode fazer em uma única expressão!
# TODO(human): Complete a expressão:

# Mas ANTES de escrever o código, responda:
# - Qual é o shape esperado?
# - O shape esperado é: (,6)

# - Os valores estarão entre 0 e 1?
# - Após a normalização sim

# - Qual seria o valor mínimo (temperatura mais fria)?
# - O Valor minimo é: C:18.9 F:66.02 Nomralizado: 0
# - Qual seria o valor máximo (temperatura mais quente)?
# - O valor máximo é: C:25.1 F:77.18 Normalizado: 1

temp_fahrenheit = temp_celsius * 1.8 + 32
temp_normalizada = (temp_fahrenheit - temp_fahrenheit.min()) / (temp_fahrenheit.max() - temp_fahrenheit.min())

print(f"Temperaturas em fahrenheit: \n{temp_fahrenheit}\n")
print(f"Temperaturas normalizadas:\n{temp_normalizada}\n")
print(f"Shape: {temp_normalizada.shape}")
print(f"Min: {temp_normalizada.min()}, Max: {temp_normalizada.max()}\n")

# Pergunta: qual é o valor normalizado de 20.5°C?
# Responda usando índice [0]
print(f"20.5°C normalizado: {temp_normalizada[0]}\n")


# %%
print("\n=== 2. MÉTODOS DE UFUNC: reduce() ===\n")

# reduce() aplica uma operação de forma cumulativa aos elementos
# Exemplo: np.add.reduce([1, 2, 3, 4]) = ((1+2)+3)+4 = 10

vendas_diarias = np.array([150, 200, 175, 300, 250, 180])
print(f"Vendas diárias:\n{vendas_diarias}\n")

# TODO(human): Use np.add.reduce() para calcular a soma total
# Dica: a função é np.add (adição é uma ufunc)
total_vendas = np.add.reduce(vendas_diarias)
print(f"Total de vendas (com reduce): {total_vendas}\n")

# Pergunta: qual é o resultado?
# Resposta: O resultado é: 1255

# Qual a diferença com np.sum()?
# Não existe uma diferencia entre o add.reduce e sum, o resultado será o mesmo mas o reduce pode ser utilizado também com multiplicação divisão

# Responda: reduce() é mais didático mas sum() é mais rápido/legível
# Não necessariamente


# %%
print("\n=== 3. MÉTODOS DE UFUNC: accumulate() ===\n")

# accumulate() retorna o resultado PARCIAL de cada passo
# Exemplo: np.add.accumulate([1, 2, 3, 4]) = [1, 1+2, 1+2+3, 1+2+3+4]

# TODO(human): Use np.add.accumulate() para obter a soma parcial (cumulativa)
vendas_acumuladas = np.add.accumulate(vendas_diarias)
print(f"Vendas acumuladas:\n{vendas_acumuladas}\n")
print(f"Shape: {vendas_acumuladas.shape}\n")

# Pergunta: qual é o último valor?
# Resposta: 1255

# É igual ao total_vendas calculado com reduce()?
# O ultimo elemento é igual,mas a diferencia é que ele soma em todos os passos enquanto o reduce retorna apenas o resultado final
# %%
print("\n=== 4. MÉTODOS DE UFUNC: outer() ===\n")

# outer() aplica a operação entre TODOS os pares de elementos
# Exemplo: np.multiply.outer([1, 2], [3, 4]) = [[1*3, 1*4], [2*3, 2*4]]

a = np.array([1, 2, 3])
b = np.array([10, 20])

print(f"Array A: {a}")
print(f"Array B: {b}\n")

# TODO(human): Use np.multiply.outer() para criar uma tabela de multiplicação
# Antecipe:
# - Qual será o shape? (dica: len(a) × len(b))
# - O shape será de (3,2)

# - Qual será o primeiro elemento?
# - O primeiro elemento será 10

# - Qual será o último elemento?
# - O ultimo elemento será 60

tabela_mult = np.multiply.outer(a, b)
print(f"Tabela de multiplicação (outer):\n{tabela_mult}\n")
print(f"Shape: {tabela_mult.shape}\n")

# %%
print("\n=== 5. FUNÇÕES MATEMÁTICAS: Trigonometria ===\n")

# Simular um sinal senoidal (onda)
# Use np.sin(), np.cos(), np.tan()

x = np.linspace(0, 2*np.pi, 8)  # 8 pontos de 0 a 2π
print(f"Eixo X (radianos):\n{x}\n")

# TODO(human): Calcule o seno de cada valor
# Use np.sin(x)
seno = np.sin(x)
print(f"sen(x):\n{seno}\n")

# TODO(human): Calcule o cosseno de cada valor
# Use np.cos(x)
cosseno = np.cos(x)
print(f"cos(x):\n{cosseno}\n")

# Pergunta:
# - Em qual índice o seno é máximo (≈1)?
# - O indice seno maximo é o indice 7

# - Em qual índice o cosseno é máximo (≈1)?
# - O indice cosseno maximo é o 0 e 7

# - Qual é a relação entre sin² + cos² para cada ponto?
# - para cada ponto do array, a soma do seno ao quadrado com o cosseno ao quadrado deve ser igual a 1

print(f"Array x tem {len(x)} elementos")
print(f"Índices válidos: {list(range(len(x)))}")
print(f"Seno máximo está em: {np.argmax(seno)}")
print(f"Cosseno máximo está em: {np.argmax(cosseno)}")

print(f"Valores de x:\n{x}")
print(f"\nSeno dos valores:\n{seno}")
print(f"\nSeno máximo está no índice: {np.argmax(seno)}")
print(f"Valor do ângulo nesse índice: {x[np.argmax(seno)]}")
print(f"Valor do seno nesse índice: {seno[np.argmax(seno)]}")

# %%
print("\n=== 6. FUNÇÕES MATEMÁTICAS: Logaritmo e Exponencial ===\n")

# Simular crescimento exponencial (população, juros)
anos = np.array([0, 1, 2, 3, 4, 5])
crescimento_exp = 1000 * np.exp(0.2 * anos)  # P = P0 * e^(kt)


print(f"Anos: {anos}")
print(f"População (e^0.2t):\n{crescimento_exp}\n")

# TODO(human): Use np.log() para calcular o logaritmo natural de cada valor
# Isso é o INVERSO da exponencial
log_populacao = np.log(crescimento_exp)
teste_ln = np.exp(log_populacao)
print(f"ln(população):\n{log_populacao}\n")
print(f"{teste_ln}")
# Pergunta:
# - Qual é a relação entre população original e ln(população)?
# - a relação é a prova real entre o logaritmo e exponencial

# - Se fizer exp(ln(população)), volta ao original?
# - Sim, volta ao original

# %%
print("\n=== 7. OPERAÇÕES CONDICIONAIS: np.where() ===\n")

# np.where(condição, valor_se_true, valor_se_false)
# Tipo: IF THEN ELSE vetorizado

notas = np.array([7.5, 8.2, 5.3, 6.1, 9.0, 4.8])
print(f"Notas:\n{notas}\n")

# TODO(human): Use np.where() para classificar:
# - "APROVADO" se nota >= 6.0
# - "REPROVADO" se nota < 6.0
# Dica: np.where(notas >= 6.0, "APROVADO", "REPROVADO")

status = np.where(notas >= 6.0, "APROVADO", "REPROVADO")
print(f"Status dos alunos:\n{status}\n")
print(f"Tipo do Status: {status.dtype}")

# Pergunta: qual é o dtype do resultado?
# Resposta: O dtype é do tipo string

# %%
print("\n=== 8. COMPARAÇÃO PRÁTICA: LOOP vs VETORIZAÇÃO ===\n")

# Tarefa: converter 1 milhão de temperaturas K para Celsius
np.random.seed(42)
temps_kelvin = np.random.uniform(273, 373, 1_000_000)

print(f"Dataset: {temps_kelvin.shape[0]:,} medições\n")

# Método 1: LOOP Python (lento)
inicio_loop = time.time()
resultado_loop = []
for temp in temps_kelvin:
    celsius = temp - 273.15
    resultado_loop.append(celsius)
resultado_loop = np.array(resultado_loop)
tempo_loop = time.time() - inicio_loop

print(f"Loop Python: {tempo_loop:.6f} segundos")
print(f"Resultado loop:  \n{resultado_loop}\n")
# Método 2: Vetorização (rápido)
# TODO(human): Faça a mesma operação sem loop
inicio_vetorizado = time.time()
resultado_vetorizado = temps_kelvin - 273.15
tempo_vetorizado = time.time() - inicio_vetorizado

print(f"Vetorização: \n{tempo_vetorizado:.6f} segundos")
print(f"Resultado Vetorizado: \n{resultado_vetorizado}\n")

# Comparação
speedup = tempo_loop / tempo_vetorizado
print(f"\nSpeedup: {speedup:.1f}x mais rápido!\n")

# Validação
print(f"Resultados idênticos? {np.array_equal(resultado_loop, resultado_vetorizado)}")

# %%
print("\n=== 9. DESAFIO FINAL: Composição Completa ===\n")

# Dados brutos de sensores de pressão
pressao_psi = np.array([14.5, 15.2, 14.8, 16.1, 13.9, 15.5])
print(f"Pressão (PSI):\n{pressao_psi}\n")

# TODO(human): Realize as transformações em sequência:
# 1. Converter PSI para Pascal (1 PSI = 6894.76 Pa)
# 2. Normalizar entre 0-100 (min = 0, max = 100)
# 3. Aplicar log natural (para escala logarítmica)
# 4. Classificar em categorias usando np.where():
#    - "Baixa" se log(pressão) < 11.0
#    - "Normal" se 11.0 <= log(pressão) < 11.3
#    - "Alta" se log(pressão) >= 11.3
# Antecipe:
# - Qual será o dtype final?
# - Qual será o shape final?

pressao_pa = pressao_psi * 6894.76
pressao_normalizada = (pressao_pa - pressao_pa.min()) / (pressao_pa.max() - pressao_pa.min()) * 100
pressao_log = np.log(pressao_pa)

pressao_categoria = np.where(pressao_log < 11.0, "Baixa",
                              np.where(pressao_log < 11.3, "Normal", "Alta"))

print(f"Pressão (Pa):\n{pressao_pa}\n")
print(f"Pressão normalizada (0-100):\n{pressao_normalizada}\n")
print(f"Pressão (log):\n{pressao_log}\n")
print(f"Categorias:\n{pressao_categoria}\n")

# ============================================================================
# PRÓXIMOS PASSOS
# ============================================================================
# Implemente os TODOs acima e responda às perguntas.
# Depois: Broadcasting (Módulo 7) e Agregações (Módulo 8).
