# %%
import numpy as np

# %%

temperaturas = np.array([
    [20.5, 21.0, 19.8, 22.1],  # sensor 1
    [18.9, 19.5, 20.2, 21.0],  # sensor 2
    [22.0, 21.8, 23.1, 22.5]   # sensor 3
])

print(temperaturas[1, [0,2]])
print(temperaturas[1, 0:4:3])
print(temperaturas[0:2])
valores_altos = temperaturas > 21
print(temperaturas[valores_altos])
print(temperaturas[valores_altos].shape)
print(len(temperaturas[valores_altos]))
print(temperaturas[temperaturas >= 21.5])
print(temperaturas[temperaturas >= 21.5].shape)
print(len(temperaturas[temperaturas >= 21.5]))

# %%
temps_corrigidas = temperaturas.copy()
temps_corrigidas

# %%
# 1. Qual o código você escreveria para substituir os valores < 19.5
temps_corrigidas[temps_corrigidas < 19.5] = 19.5
temps_corrigidas

# %%
# 2. Quantos valores foram modificados
print(f"Valores modificados: {len(temperaturas[temperaturas < 19.5])}")
print(f"Valores modificados: {temperaturas != temps_corrigidas}")
# 3 Por que usamos .copy() ao invés de trabalhar direto em temperaturas
# sempre devemos usar o copy pois não devemos alterar/modificar o array original