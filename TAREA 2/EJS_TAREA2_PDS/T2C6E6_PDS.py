"PDS Tarea 2 Ejersicio6:"

"""
Ejercicio 6: Encontrar una frecuencia oculta
Señal observada: x(t) = 2*sin(2*pi*7*t)
Frecuencias candidatas: {3, 5, 7, 9, 11} Hz
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------- Función de correlación cruzada ----------
def correlacion_cruzada(x, y):
    """Calcula la correlación cruzada Rxy[k] = sum x[n]*y[n+k]."""
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
fs = 100.0                  # Frecuencia de muestreo (Hz)
t = np.arange(0, 2, 1/fs)   # 2 segundos
x = 2 * np.sin(2 * np.pi * 7 * t)   # Señal observada

frecuencias = [3, 5, 7, 9, 11]      # Candidatas

# ---------- Cálculo de correlaciones ----------
max_corrs = []
for f in frecuencias:
    r = np.sin(2 * np.pi * f * t)   # Referencia corregida: sin(2*pi*f*t)
    R, _ = correlacion_cruzada(x, r)
    max_corrs.append(np.max(np.abs(R)))

# ---------- Resultados en consola ----------
print("=" * 50)
print("Ejercicio 6: Encontrar una frecuencia oculta")
print("=" * 50)
print(f"{'Frecuencia (Hz)':>18} | {'Máx |Correlación|':>18}")
print("-" * 50)
for f, c in zip(frecuencias, max_corrs):
    print(f"{f:>18} | {c:>18.2f}")

f_detectada = frecuencias[int(np.argmax(max_corrs))]
print(f"\nFrecuencia detectada: {f_detectada} Hz")

# ---------- Gráfica ----------
plt.figure(figsize=(8, 5))
plt.stem(frecuencias, max_corrs, basefmt=" ")
plt.title("Ejercicio 6: Magnitud de correlación vs frecuencia candidata")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Máx |Correlación|")
plt.grid(True)
plt.tight_layout()
plt.show()
