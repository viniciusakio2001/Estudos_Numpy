# %%
import numpy as np

# ============================================================================
# MÓDULO 6 — OPERAÇÕES VETORIZADAS
# ============================================================================
#
# O objetivo: realizar operações em TODOS os elementos de um array
# sem usar loops Python explícitos.
#
# Conceito chave: NumPy aplica operações elemento a elemento (broadcasting)
# automaticamente.
#
# ============================================================================
# %%
print("\n=== 1. OPERAÇÕES ARITMÉTICAS BÁSICAS ===\n")

# Exemplo: medições de temperatura em 5 sensores
temps = np.array([20.5, 21.3, 19.8, 25.1, 18.9])
print(f"Temperaturas originais:\n{temps}\n")

# Pergunta: qual é o shape e dtype deste array?
print(f"Shape: {temps.shape}")
print(f"Dtype: {temps.dtype}")
print()

# TODO(human): Conversão de Celsius para Fahrenheit
# Fórmula: F = C * 1.8 + 32
# Realize a conversão SEM usar loops
temps_fahrenheit = temps * 1.8 + 32
print(f"Temperaturas em Fahrenheit (sua solução):\n{temps_fahrenheit}\n")
print(f"Shape das temperaturas fahrenheit: {temps_fahrenheit.shape}")
# Depois que implementar, responda:
# - Qual é o shape de temps_fahrenheit?
# - O Shape é:  (5,) mantendo a mesma estrutura porém com valores em fahrenheit

# - O resultado é um escalar ou um array
# - O resultado é um array

# - Quantos valores diferentes você obteve?
# - Todos os valores são diferentes das temperaturas em fahrenheit


# %%
print("\n=== 2. COMPARAÇÕES VETORIZADAS ===\n")

# Já você tem experiência com isso do Módulo 4 (indexação booleana)
# Mas agora vamos explorar mais a fundo.

velocidades = np.array([5.2, 8.1, 3.4, 9.8, 7.5, 4.1])
print(f"Velocidades (m/s):\n{velocidades}\n")

# TODO(human): Crie uma máscara booleana para "velocidade > 6"
mascara_alta = velocidades > 6
print(f"Máscara (velocidade > 6):\n{mascara_alta}")
print(f"Shape da máscara: {mascara_alta.shape}")
print(f"Dtype da máscara: {mascara_alta.dtype}\n")

# Pergunta: qual é o shape da máscara? Por que não muda?
# Resposta: O shape da mascara é (6,), não muda pois ele retornar como true o que é maior que 6 e caso ao contrário ira colocar como false os valores menor que 6 não mudando o shape em si

# TODO(human): Use a máscara para extrair apenas velocidades > 6
velocidades_altas = velocidades[mascara_alta]
print(f"Velocidades altas (seu resultado):\n{velocidades_altas}\n")
print(f"Velocidade Altas (shape): {velocidades_altas.shape}")
print(f"Velocidade Altas (tamanho): {velocidades_altas.size}")

# - Qual é o shape de velocidades_altas? (não será (6,) — será reduzido)
# - O shape de velocidades alta será de (3,)

# - Por que o shape mudou? (porque filtramos com a máscara)
# - Por agora o shape só mostra valores maiores que 6

# - Quantos elementos você extraiu? (conte manualmente ou use .size)
# - Extrai 3 elementos 

# %%
print("\n=== 3. OPERAÇÕES LÓGICAS (& E |) ===\n")

# Combinações de condições
umidade = np.array([45, 72, 38, 85, 60, 92, 48, 65])
temperatura = np.array([20, 24, 18, 26, 22, 28, 19, 23])

print(f"Umidade: {umidade}")
print(f"Temperatura: {temperatura}\n")

# Condição: Umidade >= 70 E Temperatura <= 25
# (clima favorável para crescimento de mofo)

# TODO(human): Combine as duas condições usando &
# Dica: use parênteses em cada condição!
mascara_mofo = (umidade >= 70) & (temperatura <= 25)
print(f"Índices com risco de mofo:\n{np.where(mascara_mofo)[0]}\n")

# Pergunta: quantos pontos têm risco? Qual é a forma esperada?
# Resposta: Somenete o indice 1 (72,24), unico indice que passam da unidade de 70 e temperatura menor que 25

# %%
print("\n=== 4. OPERAÇÕES EM-PLACE (modificar array original) ===\n")

# Valores de pressão (Pa) que devem ser reduzidos em 10%
pressao = np.array([101325, 101200, 101150, 101300], dtype=np.float32)
print(f"Pressão original (dtype={pressao.dtype}):\n{pressao}\n")

# Método 1: Atribuição normal (cria novo array)
pressao_reduzida = pressao * 0.9
print(f"Método 1 - Cria novo array:\n{pressao_reduzida}\n")

# Método 2: Operação in-place (modifica original)
# Sintaxe: arr *= valor
# TODO(human): Modifique pressao IN-PLACE multiplicando por 0.9
pressao *= 0.9
print(f"Método 2 - Modifica original:\n{pressao}\n")

# Pergunta: qual é a diferença entre os dois métodos?
# Resposta: não existe uma diferencia em si mas sim do jeito que ela executando (uma modifica a original e a ouutra é armazenada em outra variavel)

# Qual é mais rápido? Quando usar cada um?
# não que in-place seja mais rápido mas economiza RAM.

# %%
print("\n=== 5. FUNÇÕES MATEMÁTICAS UNIVERSAIS ===\n")

# Valores de amplitude em um sinal
amplitudes = np.array([-3.5, 2.1, -1.8, 4.2, -0.5])
print(f"Amplitudes (com negativos):\n{amplitudes}\n")

# TODO(human): Calcule o valor absoluto SEM usar abs()
# Use np.abs()
valores_abs = np.abs(amplitudes)
print(f"Valores absolutos:\n{valores_abs}\n")

# TODO(human): Calcule a raiz quadrada de cada valor absoluto
# Use np.sqrt()
raizes = np.sqrt(valores_abs)
print(f"Raízes quadradas:\n{raizes}\n")

# TODO(human): Calcule 2^x para cada amplitude
# Use np.power(2, arr) ou np.exp2(arr)
potencias = np.power(2, amplitudes)
print(f"2^amplitude:\n{potencias}\n")


# %%
print("\n=== 6. COMPARAR: LOOP PYTHON vs VETORIZAÇÃO ===\n")

# Dataset: 10.000 medições de sensores
np.random.seed(42)
dados_brutos = np.random.uniform(0, 100, 10000)

print(f"Array com {dados_brutos.shape[0]} elementos\n")

# Versão 1: Converter para Celsius (Tk - 273) usando LOOP
# Esta será mais lenta
resultado_loop = []
for valor in dados_brutos:
    resultado_loop.append(valor - 273)
resultado_loop = np.array(resultado_loop)

# Versão 2: Vetorizada (sua tarefa)
# TODO(human): Faça a mesma operação sem loop
# Apenas: resultado_vetorizado = dados_brutos - 273
resultado_vetorizado = dados_brutos - 273

# Verifique se os resultados são iguais
print(f"Resultados são idênticos? {np.array_equal(resultado_loop, resultado_vetorizado)}")
print(f"Ambas têm shape {resultado_loop.shape}?\n")
print(f"""{resultado_vetorizado.shape == resultado_loop.shape}""")
# A versão vetorizada é ~100x mais rápida!
# Não vamos medir agora, mas é importante saber.

# ============================================================================
# PRÓXIMOS PASSOS
# ============================================================================
# Implemente os exercícios acima e responda às perguntas.
# Depois, fornecerei mais operações e conceitos avançados.
