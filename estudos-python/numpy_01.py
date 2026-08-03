# %%
import numpy as np

# %%
print(np.__version__)

# %%
lista = [7.5, 8.0, 6.5, 9.0, 5.5]
notas = np.array(lista)
print(notas)
print(type(notas))

# %%
# criar arrays com valores especificos
zeros = np.zeros(7)
uns = np.ones(7)
# sequencial em passos
seq = np.arange(0, 16, 2)
# Dividir do 0 a 16 em 7 quantidade
lins = np.linspace(0, 16, 7)
# Criar Matriz identidade 3x3 diagonal
i = np.eye(3)
print(zeros)
print(uns)
print(seq)
print(lins)
print(i)

