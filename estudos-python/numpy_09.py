# %%
import numpy as np

# %%
logaritimo = np.logspace(0,2,3)
print(logaritimo)

# %%
print(np.logspace(1,4,5))
print(np.logspace(1,4,5).shape)
print(np.logspace(1,4,5).dtype)
print(np.logspace(1,4,5).size)


# %%
zeross = np.zeros(5)
oness = np.ones(10)
arr_full = np.full((2,3), 5)

# %%
arr_zeros = np.zeros_like(zeross)
arr_ones = np.ones_like(oness)
arr_fulls = np.full_like(arr_full, 99)

print(f"{arr_zeros} \n {arr_ones} \n {arr_fulls}")


# %%
sensores = np.array([23.5, 19.2, 25.8])

arr_zeros = np.zeros_like(sensores)
flags_sensores = np.full_like(sensores, 1)

print(f"{arr_zeros} \n {flags_sensores}")