"PDS Tarea 2 Ejersicio10:"

"""
Ejercicio 10: Build a frequency detector
Función: detect_frequencies(x, fs, frequencies)
Señal de prueba:
x(t) = 1.5*sin(2*pi*4*t) + 0.7*sin(2*pi*9*t + pi/4) + 2*sin(2*pi*16*t - pi/3)
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


# ---------- Detector de frecuencias ----------
def detect_frequencies(x, fs, frequencies):
    """
    Detecta la presencia de cada frecuencia candidata en x.

    Parámetros:
        x : array con la señal muestreada
        fs : frecuencia de muestreo (Hz)
        frequencies : lista de frecuencias candidatas (Hz)

    Retorna:
        medidas : array con la magnitud de correlación para cada frecuencia
    """
    N = len(x)
    n = np.arange(N)
    medidas = []

    for f in frequencies:
        # Referencias seno y coseno (independientes de fase)
        r_sin = np.sin(2 * np.pi * f * n / fs)
        r_cos = np.cos(2 * np.pi * f * n / fs)

        R_sin, _ = correlacion_cruzada(x, r_sin)
        R_cos, _ = correlacion_cruzada(x, r_cos)

        max_sin = np.max(np.abs(R_sin))
        max_cos = np.max(np.abs(R_cos))

        # Magnitud independiente de fase
        mag = np.sqrt(max_sin**2 + max_cos**2)
        medidas.append(mag)

    return np.array(medidas)


# ---------- Parámetros ----------
fs = 100.0
t = np.arange(0, 2, 1/fs)

x = (1.5 * np.sin(2 * np.pi * 4 * t)
     + 0.7 * np.sin(2 * np.pi * 9 * t + np.pi / 4)
     + 2.0 * np.sin(2 * np.pi * 16 * t - np.pi / 3))

frecuencias = list(range(1, 21))

# ---------- Gráfica de la señal original ----------
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title("Ejercicio 10: Señal de prueba")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Detección ----------
medidas = detect_frequencies(x, fs, frecuencias)

# ---------- Resultados ----------
print("=" * 60)
print("Ejercicio 10: Detector de frecuencias")
print("=" * 60)
print(f"{'Frecuencia (Hz)':>18} | {'Medida de presencia':>22}")
print("-" * 60)
for f, m in zip(frecuencias, medidas):
    print(f"{f:>18} | {m:>22.2f}")

# Ranking de las tres frecuencias dominantes
idx_ordenados = np.argsort(medidas)[::-1]
print("\nTres frecuencias dominantes (ranking):")
for i in range(3):
    idx = idx_ordenados[i]
    print(f"  {i+1}) {frecuencias[idx]} Hz  (medida = {medidas[idx]:.2f})")

# ---------- Gráfica del detector ----------
plt.figure(figsize=(10, 5))
plt.stem(frecuencias, medidas, basefmt=" ")
plt.title("Ejercicio 10: Respuesta del detector vs frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Medida de presencia")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nNota: El detector usa referencias seno y coseno para ser")
print("independiente de la fase de la señal. Una sola referencia")
print("(solo seno) fallaría si la señal estuviera en cuadratura.")