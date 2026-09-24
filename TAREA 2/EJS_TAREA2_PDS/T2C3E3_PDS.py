"PDS Tarea 2 Ejersicio3:"
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 0, 1, -1, 2, 1, -1, 0, 0])
p = np.array([1, -1, 2, 1, -1])

Nx, Np = len(x), len(p)
Rxp = []
lags_xp = range(-(Np-1), Nx)

for k in range(-(Np-1), Nx):
    suma = 0
    for n in range(Nx):
        if 0 <= n+k < Np:
            suma += x[n] * p[n+k]
    Rxp.append(suma)

Rxp = np.array(Rxp)
lags_xp = np.array(list(lags_xp))

plt.figure(figsize=(10, 4))
plt.stem(lags_xp, Rxp, basefmt=" ")
plt.title("Correlación cruzada Rxp[k]")
plt.xlabel("Lag k")
plt.ylabel("Rxp[k]")
plt.grid(True)
plt.show()

