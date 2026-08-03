# %%
import numpy as np

# %%
temperaturas = np.linspace(15,35,24)
arr_temp = np.full((10,24),temperaturas, dtype='float64')
print(arr_temp)

print(arr_temp.shape)
print(arr_temp.dtype)
print(arr_temp.nbytes)
print(arr_temp.nbytes / 1000000)

temperaturas_f32 = arr_temp.astype('float32')
print(temperaturas_f32)
print(temperaturas_f32.nbytes)
print(arr_temp.nbytes - temperaturas_f32.nbytes)


# %%
valor_original = 22.82608696
valor_f32 = np.float32(valor_original)

print(f"Original (floa64): {valor_original}")
print(f"convertido (float32): {valor_f32}")
print(f"Diferencia: {abs(valor_original - valor_f32)}")