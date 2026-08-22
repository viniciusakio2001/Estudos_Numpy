# %%
import numpy as np


# %% 
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

arr_transpost = arr_2d.transpose()
arr_transpost

# %%
dados =  np.arange(12).reshape(3,4)
print(f"""Original Shape:
{dados.shape}

{dados}""")

# %%
# MÓDULO 5 — Alteração e organização de arrays
# Tópico: squeeze() e expand_dims()

# %%
# Exercício 1: squeeze() — remover dimensões de tamanho 1
print("=== EXERCÍCIO 1: squeeze() ===")

# Simulando leitura de dados de 3 sensores em 1 medição
dados_sensores = np.array([[[25.5, 30.2, 28.1]]])  # shape: (1, 1, 3)
print(f"Shape original: {dados_sensores.shape}")
print(f"Dados: {dados_sensores}")



# TODO(human): Use squeeze() para remover as dimensões de tamanho 1
# Atribua o resultado a uma variável chamada 'dados_limpos'
dados_limpos = dados_sensores.squeeze()
# Depois mostre o shape e os dados
print(f"Shape com squeeze:  {dados_limpos.shape}")
print(f"Dados com squeeze: {dados_limpos}")

# %%
# Exercício 2: expand_dims() — adicionar uma dimensão
print("\n=== EXERCÍCIO 2: expand_dims() ===")

# Uma leitura de 3 sensores
leitura = np.array([25.5, 30.2, 28.1])  # shape: (3,)
print(f"Shape original: {leitura.shape}")
print(f"Dados: {leitura}")

# TODO(human): Use expand_dims(leitura, axis=0) para adicionar uma dimensão no início
# Atribua o resultado a 'leitura_2d'
leitura_2d = np.expand_dims(leitura, axis=0)
# Depois mostre o shape e os dados
print(f"resultado com expand: {leitura_2d}")
print(f"shape com expand: {leitura_2d}")

# %%
# Exercício 3: Entender axis na expand_dims()
print("\n=== EXERCÍCIO 3: Diferentes axis ===")

# Mesmo array anterior
leitura = np.array([25.5, 30.2, 28.1])  # shape: (3,)

# TODO(human): Crie duas versões:
# 1. expand_dims(leitura, axis=0) — atribua a 'expanded_axis0'
expanded_axis0 = np.expand_dims(leitura, axis=0)
print(f"expanded_axix0(array): {expanded_axis0}")
print(f"expanded_axix0(shape): {expanded_axis0.shape}")

# 2. expand_dims(leitura, axis=1) — atribua a 'expanded_axis1'
expanded_axis1 = np.expand_dims(leitura, axis=1)
print(f"expanded_axis1: {expanded_axis1}")
print(f"expanded_axis1: {expanded_axis1.shape}")

# Para cada uma, mostre shape e dados
# Depois responda: Qual é a diferença entre axis=0 e axis=1?
""" Resposta: A diferencia entre axis=0 e axis1 é que no axis=0 ele mantem
as colunas de acordo com o array original e o axis1 ele inclui a quantidade de dimensão
de acordo com a quantidade de colunas que possuia no array original 
"""
# %%
array_exemplo = np.array([[[0,1,2,3,4,5,6,7]]])
print(f"array Original: {array_exemplo}")
print(f"shape original: {array_exemplo.shape}")
array_limpo = array_exemplo.squeeze()
print(f"array com squeeze: {array_limpo}")
print(f"Shape com squeeze: {array_limpo.shape}")


# %%

# uso:
array_1 = np.arange(20)
print(f"array original: {array_1}")
print(f"shape original: {array_1.shape}")
# necessário passar o parâmetro axis
array_2d = np.expand_dims(array_1, axis=0)
print(f"array com expand: {array_2d}")
print(f"array com expand: {array_2d.shape}")

# %%
# EXERCÍCIO 4: newaxis — sintaxe alternativa para expand_dims()
print("\n=== EXERCÍCIO 4: newaxis ===")

leitura = np.array([25.5, 30.2, 28.1])  # shape: (3,)
print(f"Original shape: {leitura.shape}")

# newaxis é um atalho para expand_dims
# leitura[np.newaxis, :] é equivalente a expand_dims(leitura, axis=0)
leitura_newaxis = leitura[np.newaxis, :]
print(f"Com newaxis [np.newaxis, :] shape: {leitura_newaxis.shape}")
print(f"Dados: {leitura_newaxis}")

# TODO(human): Use newaxis para criar uma coluna (shape (3, 1))
leitura_coluna = leitura[:, np.newaxis]
# Dica: use leitura[:, np.newaxis] (newaxis no segundo eixo)~
print(f"shape com newaxis coluna: {leitura_coluna.shape}")
# Atribua a 'leitura_coluna' e mostre shape e dados
print(f"dados com newaxis coluna: {leitura_coluna}")

# %%
# EXERCÍCIO 5: squeeze() com parâmetro axis (opcional)
print("\n=== EXERCÍCIO 5: squeeze() com axis (opcional) ===")

arr_3d = np.array([[[1, 2, 3, 4, 5]]])  # shape: (1, 1, 5)
print(f"Original shape: {arr_3d.shape}")

# squeeze() sem parâmetro remove TODAS as dimensões de tamanho 1
arr_sem_param = arr_3d.squeeze()
print(f"squeeze() sem axis shape: {arr_sem_param.shape}")

# squeeze(axis=0) remove APENAS a dimensão 0 se tiver tamanho 1
# TODO(human): Use squeeze(axis=0) no arr_3d e atribua a 'arr_axis0'
arr_axis0 = np.squeeze(arr_3d, axis=0)
# Depois mostre o shape — deve ser (1, 5) pois remove apenas dimensão 0
print(f"axis0(shape): {arr_axis0.shape}")

# %%
array = np.arange(5)

np_tile = np.tile(array, 2)
print(np_tile)

array_2 = np.array([
    [1,2],
    [3,4]
])

print(f"array original:\n {array_2}")
tile_array2 = np.tile(array_2, (2,2))
print(f"array com tile: \n {tile_array2}")