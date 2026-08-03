# %%
import numpy as np

# %%
arr_1d = np.full((10,), 25.0)

print(arr_1d)
print(arr_1d.shape)
print(arr_1d.dtype)
print(arr_1d.nbytes)


# %%
ex_2 = np.full((3,7), fill_value=-999.9)
print(f"Array: {ex_2} \n")
print(f"Shape: {ex_2.shape} \n")
print(f"dtype: {ex_2.dtype}")
print(f"Bytes: {ex_2.nbytes}" )