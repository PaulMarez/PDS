"PDS Tarea 2 Ejersicio9:"

"""
Ejercicio 9: Detección de frecuencia en ruido blanco gaussiano
x[n] = sin(2*pi*6*n/fs) + 0.7*sin(2*pi*15*n/fs) + w[n]
fs = 100 Hz
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
N = 200
n = np.arange(N)
t = n / fs

# Señal limpia
x_clean = np.sin(2 * np.pi * 6 * n / fs) + 0.7 * np.sin(2 * np.pi * 15 * n / fs)

# ---------- Gráfica señal limpia vs ruidosa ----------
sigmas = [0.1, 0.5, 2.0]

plt.figure(figsize=(10, 5))
plt.plot(t, x_clean, 'k', label='Señal limpia', linewidth=1.5)
for sigma in sigmas:
    np.random.seed(42)
    w = np.random.normal(0, sigma, N)
    x_noisy = x_clean + w
    plt.plot(t, x_noisy, alpha=0.6, label=f'σ = {sigma}')
plt.title("Ejercicio 9: Señal limpia vs ruidosa para distintos σ")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Detección para cada σ ----------
frecuencias = list(range(1, 21))

plt.figure(figsize=(10, 6))

for sigma in sigmas:
    np.random.seed(42)
    w = np.random.normal(0, sigma, N)
    x_noisy = x_clean + w

    max_corrs = []
    for f in frecuencias:
        r = np.sin(2 * np.pi * f * n / fs)
        R, _ = correlacion_cruzada(x_noisy, r)
        max_corrs.append(np.max(np.abs(R)))

    # Detectar los dos picos más altos
    idx_ordenados = np.argsort(max_corrs)[::-1]
    f1 = frecuencias[idx_ordenados[0]]
    f2 = frecuencias[idx_ordenados[1]]

    print("=" * 60)
    print(f"Ejercicio 9: σ = {sigma}")
    print("=" * 60)
    print(f"Frecuencias detectadas: {f1} Hz y {f2} Hz")
    print(f"¿Se detectan 6 y 15 Hz? {'Sí' if {f1, f2} == {6, 15} else 'No'}")

    plt.stem(frecuencias, max_corrs, basefmt=" ", label=f'σ = {sigma}')

plt.title("Ejercicio 9: Magnitud de correlación vs frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Máx |Correlación|")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()