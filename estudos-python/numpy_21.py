# %%
import numpy as np

# %%
dados = np.arange(24)

matriz_2d = dados.reshape(4,6)
print(matriz_2d)


# %%

matriz_3d = dados.reshape(2,3,4)
print(matriz_3d)


# %%
matriz_flatten = matriz_3d.flatten()
print(matriz_flatten)

# %%
matriz_ravel = matriz_3d.ravel()
print(matriz_ravel)

# %%
matriz_ravel.shape


# %%
matriz_3d_teste = np.arange(24).reshape(2,3,4)

print(f"Original : {matriz_3d_teste[0,0,0]}")

ravel_resultado = matriz_3d_teste.ravel()
flatten_resultado = matriz_3d_teste.flatten()

# Modificar ravel
ravel_resultado[0] = 999
print(f"Modificada ravel[0] : {matriz_3d_teste[0,0,0]}")

flatten_resultado[0] = 888
print(f"Moficada flatten[0] : {matriz_3d_teste[0,0,0]}")

# %%
import numpy as np 

arr = np.arange(12).reshape(3,4)
arr_transposed = arr.T
ravel_transposto = arr_transposed.ravel()
ravel_transposto[0] = 999
print(arr_transposed[0,0])