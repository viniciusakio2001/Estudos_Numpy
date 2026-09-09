# %%
import numpy as np

# %%
temperaturas = np.array([
    [20, 22, 21, 23, 24],
    [19, 21, 20, 22, 23],
    [21, 23, 22, 24, 25],
    [18, 20, 19, 21, 22]
])

print(f"tempertuas (shape: {temperaturas.shape}): \n {temperaturas} \n")

# %%
temperaturas_max = np.max(temperaturas, axis=1)
temperaturas_min = np.min(temperaturas, axis=1)
temperaturas_max_ajustado = temperaturas_max.reshape(-1,1)
temperaturas_min_ajustado = temperaturas_min.reshape(-1,1)

print(f"temperaturas maximas por sensor:(shape: {temperaturas_max.shape}) \n {temperaturas_max} \n")
print(f"Temperaturas minimas por sensor:(shape: {temperaturas_min.shape}) \n {temperaturas_min} \n")

# %%
temperaturas_normalizacao = (temperaturas - temperaturas_min_ajustado) / (temperaturas_max_ajustado - temperaturas_min_ajustado)

print(temperaturas_normalizacao)