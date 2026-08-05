# %%
import time
import numpy as np

# %%
t1 = time.time()
z = np.zeros(1000000)
print(f"zeros: {time.time() - t1:.6f}s")

t2 = time.time()
o = np.ones(1000000)
print(f"ones: {time.time() - t2:.6f}s")

t3 = time.time()
e = np.empty(1000000)
print(f"empty: {time.time() - t3:.6f}s")

