"PDS Tarea 2 Ejersicio5:"
import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 2, 1/fs)
x = np.sin(2*np.pi*5*t)
r1 = np.sin(2*np.pi*5*t)
r2 = np.sin(2*np.pi*8*t)

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='x(t) = sin(2π·5t)')
plt.plot(t, r1, '--', label='r1(t) = sin(2π·5t)')
plt.plot(t, r2, ':', label='r2(t) = sin(2π·8t)')
plt.title("Comparación de señales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.show()

def correlacion_cruzada(x, y):
    Nx, Ny = len(x), len(y)
    R = []
    lags = range(-(Ny-1), Nx)
    for k in lags:
        suma = 0
        for n in range(Nx):
            if 0 <= n+k < Ny:
                suma += x[n] * y[n+k]
        R.append(suma)
    return np.array(R), np.array(list(lags))

Rxy1, lags1 = correlacion_cruzada(x, r1)
Rxy2, lags2 = correlacion_cruzada(x, r2)

# Máximos absolutos
max1 = np.max(np.abs(Rxy1))
max2 = np.max(np.abs(Rxy2))

print(f"Máx |Rxy1| = {max1:.2f}")
print(f"Máx |Rxy2| = {max2:.2f}")