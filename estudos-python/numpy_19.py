# %%
import numpy as np

# %%
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"Resultado shape: {arr[:, 1].shape}")
print(f"Resultado shape: {arr[1, :].shape}")
print(f"Resultado shape: {arr[1:2].shape}")