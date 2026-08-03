# %%
import numpy as np

# %%
precos = np.array([19.90, 25.50, 12.00, 34.75])
print(precos)

# %%
zeros = np.zeros(5)
print(zeros)

# %%
sequencia = np.arange(0,20,5)
print(sequencia)
# %%
pontos = np.linspace(0,1,5)
print(pontos)

# %%
listas = np.array([1,2,3])

# %%
soma_listas =listas + listas
print(soma_listas)

# %%
listasss = [1,2,3]
listas_no_array = listasss + listasss
array_misto = np.array([1, "dois", 3])
print(f"lista + lista = {listas_no_array}")
print(f"array + array =  {soma_listas}")
print(f"array mistro: {array_misto}")
print(array_misto.dtype)