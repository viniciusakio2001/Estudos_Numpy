# %%
import numpy as np

# %%
# 1. Id's de Usuários: 0 a 10000
usuarios = np.arange(1,101)
usuarios_uint16 = usuarios.astype(dtype=np.uint16)
print(usuarios_uint16)
print(f"Shape: {usuarios_uint16.shape}")
print(f"dtype: {usuarios_uint16.dtype}")
print(f"nbytes: {usuarios_uint16.nbytes}")
print(f"info: {np.iinfo(usuarios_uint16.dtype)} \n")

print(f"---------------------------------------------------------------")
# 2. Temperaturas:
temperaturas = np.linspace(-10, 50, 50)
temperaturas_float32 = temperaturas.astype(dtype=np.float32)
print(temperaturas_float32)
print(f"Shape: {temperaturas_float32.shape}")
print(f"dtype: {temperaturas_float32.dtype}")
print(f"nbytes: {temperaturas_float32.nbytes}")
print(f"nbytes: {np.finfo(temperaturas_float32.dtype)} \n")

print(f"---------------------------------------------------------------")
# 3. Contadores

contadores = np.arange(1,11)
contadores_uint32 = contadores.astype(dtype=np.uint32)
print(contadores_uint32)
print(f"Shape: {contadores_uint32.shape}")
print(f"dtype: {contadores_uint32.dtype}")
print(f"nbytes: {contadores_uint32.nbytes} \n")
print(f"nbytes: {np.iinfo(contadores_uint32.dtype)} \n")
print(f"---------------------------------------------------------------")