"PDS Tarea 2 Ejersicio7:"

"""
Ejercicio 7: Detección de dos frecuencias
x(t) = 2*sin(2*pi*5*t) + 0.8*sin(2*pi*12*t)
fs = 100 Hz, 2 segundos
Candidatas: f = {2, 3, 4, ..., 20} Hz
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- Función de correlación cruzada ----------
def correlacion_cruzada(x, y):
    Nx, Ny = len(x), len(y)
    R = []
    lags = range(-(Ny - 1), Nx)
    for k in lags:
        suma = 0.0
        for n in range(Nx):
            if 0 <= n + k < Ny:
                suma += x[n] * y[n + k]
        R.append(suma)
    return np.array(R), np.array(list(lags))


# ---------- Parámetros ----------
fs = 100.0
t = np.arange(0, 2, 1/fs)
x = 2 * np.sin(2 * np.pi * 5 * t) + 0.8 * np.sin(2 * np.pi * 12 * t)

frecuencias = list(range(2, 21))   # 2 a 20 Hz

# ---------- Gráfica de la señal ----------
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title("Ejercicio 7: x(t) = 2sin(2π·5t) + 0.8sin(2π·12t)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Correlaciones ----------
max_corrs = []
for f in frecuencias:
    r = np.sin(2 * np.pi * f * t)
    R, _ = correlacion_cruzada(x, r)
    max_corrs.append(np.max(np.abs(R)))

# ---------- Resultados ----------
print("=" * 50)
print("Ejercicio 7: Detección de dos frecuencias")
print("=" * 50)
print(f"{'Frecuencia (Hz)':>18} | {'Máx |Correlación|':>18}")
print("-" * 50)
for f, c in zip(frecuencias, max_corrs):
    print(f"{f:>18} | {c:>18.2f}")

# Detectar los dos picos más altos
idx_ordenados = np.argsort(max_corrs)[::-1]
print(f"\nFrecuencias dominantes detectadas:")
print(f"  1) {frecuencias[idx_ordenados[0]]} Hz")
print(f"  2) {frecuencias[idx_ordenados[1]]} Hz")

# ---------- Gráfica ----------
plt.figure(figsize=(10, 5))
plt.stem(frecuencias, max_corrs, basefmt=" ")
plt.title("Ejercicio 7: Magnitud de correlación vs frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Máx |Correlación|")
plt.grid(True)
plt.tight_layout()
plt.show()
