# %%
import numpy as np
# DESAFIO FINAL — Módulo 5 Completo
print("\n=== DESAFIO FINAL: Reorganização Completa ===")

# Dados brutos de um sensor com estrutura estranha
dados_brutos = np.array([[[1.5, 2.3, 3.1, 4.2]]])  # shape: (1, 1, 4)
print(f"1. Dados brutos shape: {dados_brutos.shape}")
print(dados_brutos)

# TODO(human): Realize as transformações em sequência:
# Passo 1: Remove dimensões desnecessárias (1,1,4) → (4,)
#         Use squeeze()
dados_transformados = np.squeeze(dados_brutos)
print(f"Shape dados transformados: {dados_transformados.shape}")
# Passo 2: Expande para 10 linhas (4,) → (10, 4)
#         Use expand_dims() e depois replique 10 vezes com np.tile()
#         Ou use apenas expand_dims() com axis apropriado
dados_transformados_expand = np.expand_dims(dados_transformados, axis=0)
print(f"Expandindo o array para mais uma dimensão: {dados_transformados_expand.shape}")

dados_transformados_expand_10 = np.tile(dados_transformados_expand, (10,1))
print(f"Expandindo o array para 10 dimensões: {dados_transformados_expand_10.shape}")

# Passo 3: Transpõe (10, 4) → (4, 10)
#         Use transpose() ou .T
shape_transpose = dados_transformados_expand_10.T
print(f"Shape trnaspose: {shape_transpose.shape}")

# Mostre shape e dados em cada etapa

# %%
# COMPARAÇÃO: tile com vs sem expand_dims

arr_1d = np.array([1.5, 2.3, 3.1, 4.2])  # shape: (4,)

# Opção 1: SEM expand_dims (direto)
resultado_direto = np.tile(arr_1d, (10, 1))
print(f"Direto - shape: {resultado_direto.shape}")
print(resultado_direto)
print()

# Opção 2: COM expand_dims (explícito)
arr_2d = np.expand_dims(arr_1d, axis=0)  # (4,) → (1, 4)
resultado_explicito = np.tile(arr_2d, (10, 1))
print(f"Com expand_dims - shape: {resultado_explicito.shape}")
print(resultado_explicito)
print()

# São iguais?
print(f"Resultados são idênticos? {np.array_equal(resultado_direto, resultado_explicito)}")