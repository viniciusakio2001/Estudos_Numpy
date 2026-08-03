# %%
import numpy as np

# %%
np.diag([1,1,1])


# %%
valores = np.array([10,20,30])
np.diag(valores)

# %%
pesos = np.array([5,10,15])

# %%
print(np.diag(pesos).shape)
print(np.diag(pesos))
print(f"Quantos Zeors ? {np.count_nonzero(np.diag(pesos) == 0)}")