"PDS Tarea 2 Ejersicio4:"
import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 2, 1/fs)
x = np.sin(2*np.pi*5*t)

plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title("x(t) = sin(2π·5t)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()

# Autocorrelación manual
N = len(x)
Rxx = np.zeros(2*N - 1)
lags = np.arange(-(N-1), N)

for k in range(-(N-1), N):
    suma = 0
    for n in range(N):
        if 0 <= n+k < N:
            suma += x[n] * x[n+k]
    Rxx[k + (N-1)] = suma

# Normalizar para mejor visualización
Rxx_norm = Rxx / Rxx[N-1]

plt.figure(figsize=(10, 4))
plt.plot(lags, Rxx_norm)
plt.title("Autocorrelación de x(t) = sin(2π·5t)")
plt.xlabel("Lag (muestras)")
plt.ylabel("Rxx normalizada")
plt.grid(True)
plt.show()