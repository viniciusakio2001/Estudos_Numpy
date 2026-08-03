# %%
import numpy as np

# %%
arr = np.full((3,4), 7)
print(arr)


# %%
arr1 = np.full(5,10)
arr2 = np.full((2,3), 5.5)
arr3 = np.full((3,3,2), 0)

# %%
print(f"{arr1} \n")
print(f"{arr2} \n")
print(f"{arr3} \n")

# %%
limites = np.array([30,25,35])

np.full((4,3), limites)

# %%
np.empty(3)

# %%
np.full((5,), 0)
# %%
