# %%
import numpy as np

# %%
sensor_dados = np.array([23.5, 24.1, 22.8, 25.3, 23.9])

# %%
# Array com a mesma forma preenchido com 0
z = np.zeros_like(sensor_dados)
print(z)
# Array com mesma forma prenchido com 1
o = np.ones_like(sensor_dados)
print(o)

# Array com a mesma forma preenchido com 100

p = np.full_like(sensor_dados, 100)
print(p)

# Matriz diagonal 5x5 com esses valores
md = np.diag(sensor_dados)
print(md)

# Array vazio com mesma forma da variavel sensor_dados
emp = np.empty_like(sensor_dados)
print(emp)