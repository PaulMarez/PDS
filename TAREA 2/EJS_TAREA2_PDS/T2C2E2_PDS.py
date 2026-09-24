"PDS Tarea 2 Ejersicio2:"
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 2, 1, 0])
y = np.array([0, 0, 0, 1, 2, 3, 2, 1, 0])

plt.figure(figsize=(10, 4))
plt.stem(range(len(x)), x, linefmt='b-', markerfmt='bo', basefmt=' ', label='x[n]')
plt.stem(range(len(y)), y, linefmt='r-', markerfmt='ro', basefmt=' ', label='y[n]')
plt.title("Señales x[n] y y[n]")
plt.xlabel("n")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

# Correlación cruzada manual
Nx, Ny = len(x), len(y)
Rxy = []
lags_xy = range(-(Ny-1), Nx)

for k in range(-(Ny-1), Nx):
    suma = 0
    for n in range(Nx):
        if 0 <= n+k < Ny:
            suma += x[n] * y[n+k]
    Rxy.append(suma)

Rxy = np.array(Rxy)
lags_xy = np.array(list(lags_xy))

plt.figure(figsize=(10, 4))
plt.stem(lags_xy, Rxy, basefmt=" ")
plt.title("Correlación cruzada Rxy[k]")
plt.xlabel("Lag k")
plt.ylabel("Rxy[k]")
plt.grid(True)
plt.show()

