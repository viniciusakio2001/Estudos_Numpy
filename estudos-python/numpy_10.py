# %%
import numpy as np

# %%
# 1. Criar array dados com shape (4, 8) preenchido com -1 (sem dados)
dados = np.full((4,8),fill_value=-1)

# %%
# 2. Criar array timestamps com 8 valores espaçados linearmente de 0 a 7 segundos
horarios = np.linspace(
    0,7,8, dtype='timedelta64[s]'
)
print(horarios)

# %%
# Criar array Calibração com a matriz diagonal de fatores de calibração
calibracao = [1.0, 1.05, 0.98, 1.02]

array_cal = np.diag(calibracao)
print(array_cal)