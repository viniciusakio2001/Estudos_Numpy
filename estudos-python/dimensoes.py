# %%
import numpy as np

# %%
temperaturas = np.array([
    [20.5, 21.0, 19.8, 22.1],  # sensor 1
    [18.9, 19.5, 20.2, 21.0],  # sensor 2
    [22.0, 21.8, 23.1, 22.5]   # sensor 3
])

print(temperaturas.ndim)
print(temperaturas.shape)
print(temperaturas.size)
print(temperaturas.dtype)
temperaturas.sum()