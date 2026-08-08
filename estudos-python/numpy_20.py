# %%
import numpy as np

# %%
leituras = np.array([
    [22.5, 23.1, 22.8, 24.2, 25.0],
    [23.0, 23.5, 23.2, 24.5, 25.3],
    [23.2, 23.7, 23.4, 24.7, 25.5],
    [23.1, 23.6, 23.3, 24.6, 25.4]
])

hora1 = leituras[0, :]
print(hora1)

filters = hora1 > 23.5
print(hora1)
print(hora1[filters])
print(hora1[filters].shape)

# %%
mascara = (leituras >= 24) & (leituras <= 25)
print(mascara.shape)
print(leituras[mascara])