# %%
import numpy as np

# %%
valores = [10,20,30]

a = np.array(valores, dtype=np.int8)
b = np.array(valores, dtype=np.int32)
c = np.array(valores, dtype =np.float32)
d = np.array(valores, dtype=np.bool_)

print(a, a.dtype, a.nbytes)
print(b, b.dtype, b.nbytes)
print(c, c.dtype, c.nbytes)
print(d, d.dtype, d.nbytes)


# %%
valores_2 = np.array([10.5, 20.3, 30.9, 40.1])
valores_int32 = valores_2.astype(np.int32)
valores_uint8 = valores_2.astype(np.uint8)
valores_bool = valores_2.astype(bool)
print(f"valores originais: {valores_2}")
print(f"int32: {valores_int32}")
print(f"uint8: {valores_uint8}")
print(f"bool: {valores_bool}")

# %%
print(f"minimo int8: {np.iinfo(np.int8).min}")
print(f"Maximo int8: {np.iinfo(np.int8).max}")
print(f"Quantidade de Bits: {np.iinfo(np.int8).bits}")

print("===============================")

print(f"Minimo Float32: {np.finfo(np.float32).min}")
print(f"Maximo Float32: {np.finfo(np.float32).max}")
print(f"Precisão: {np.finfo(np.float32).eps}")

# %%

# 1. Qual é o máximo de um int16?
print(f"O máximo de um int16 é: {np.iinfo(np.int16).max}")

# 2. Qual o minimo de um uint32
print(f"O Minimo de um uint32 é: {np.iinfo(np.uint32).min}")

# 3. Qual é a precisão (eps) de um float64
print(f"A Precisão de um float64 é: {np.finfo(np.float64).eps}")

# %%
arr = np.array([127], dtype=np.int)
arr = arr + 1
print(arr)

# %%
x = np.array([10], dtype=np.int8)
y = np.array([20.5], dtype=np.float32)
z = x + y

print(f"x dtype: {x.dtype}")
print(f"y dtype: {y.dtype}")
print(f"z dtype: {z.dtype}")
print(f"Resultado: {z}")