"PDS Tarea 2 Ejersicio1:"
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 2, 1])

# Autocorrelación manual (sin usar np.correlate)
N = len(x)
Rxx = np.zeros(2*N - 1)
lags = np.arange(-(N-1), N)

for k in range(-(N-1), N):
    suma = 0
    for n in range(N):
        if 0 <= n+k < N:
            suma += x[n] * x[n+k]
    Rxx[k + (N-1)] = suma

print("Lags:", lags)
print("Rxx:", Rxx)# -*- coding: utf-8 -*-

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].stem(range(N), x, basefmt=" ")
ax[0].set_title("Señal x[n]")
ax[0].set_xlabel("n")
ax[0].set_ylabel("Amplitud")
ax[0].grid(True)

ax[1].stem(lags, Rxx, basefmt=" ")
ax[1].set_title("Autocorrelación Rxx[k]")
ax[1].set_xlabel("Lag k")
ax[1].set_ylabel("Rxx[k]")
ax[1].grid(True)

plt.tight_layout()
plt.show()