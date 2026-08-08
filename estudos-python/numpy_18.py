# %%
import numpy as np

# %%
leituras = np.array([22.5, 23.1, 22.8, 24.2, 25.0,24.5, 23.9, 23.2, 22.1, 21.8])

# %%
# 1. Imprima a primeira leitura
print(f"Imprimindo a primeira leitura: {leituras[0]}")

# 2. Imprima a ultima leitura
print(f"Imprimindo a ultima leitura: {leituras[-1]}")

# 3. Imprima as leituras de indice 2 a 5 (inclusive)
print(f"imprimindo as leituras de 2 a 5 : {leituras[2:6]}")

# 4. Imprima todas as leituras a partir do 5º indice
print(f"Imprimindo todas as leituras a partir do indice 5° {leituras[5:]}")

# %. Imprima as leituras em ordem inversa
print(f"Imprimindo as leituras em ordem inversa: {leituras[::-1]}")

# %%
# Imprimindo todas as leitruras da dimensão 1
