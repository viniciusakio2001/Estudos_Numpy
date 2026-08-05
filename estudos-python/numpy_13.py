# %%
import numpy as np

# %%
arr_1 = np.eye(4)

print(arr_1)
print(arr_1.shape)
print(arr_1.dtype)
print(np.sum(arr_1))


# %%
arr_2 = np.eye(4)
arr_3 = np.identity(4)

print(arr_2)
print(arr_3)
print(arr_3.dtype)
print(arr_2.dtype)


# %%
e = np.eye(3,5)
print(e)
print(e.shape)

# %%
valores = np.array([5,10,15])
arr_4 = np.diag(valores)
print(arr_4)

# %%
print(np.diag(arr_4))


# %%
arr_5 = np.full((2,5), 42)
print(arr_5)
print(arr_5.shape)
print(arr_5.dtype)
print(np.sum(arr_5))


# %%
dados = np.array([10, 20, 30, 40])
print(np.zeros_like(dados))
print("====================")
print(np.ones_like(dados))

