"PDS Tarea 2 Ejersicio8:"

"""
Ejercicio 8: Fase y detección sinusoidal
x1(t) = sin(2*pi*8*t)
x2(t) = sin(2*pi*8*t + pi/3)
Referencias: rs(t) = sin(2*pi*8*t), rc(t) = cos(2*pi*8*t)
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

x1 = np.sin(2 * np.pi * 8 * t)
x2 = np.sin(2 * np.pi * 8 * t + np.pi / 3)
rs = np.sin(2 * np.pi * 8 * t)
rc = np.cos(2 * np.pi * 8 * t)

# ---------- Gráfica de señales ----------
plt.figure(figsize=(10, 5))
plt.plot(t, x1, label='x1(t) = sin(2π·8t)')
plt.plot(t, x2, '--', label='x2(t) = sin(2π·8t + π/3)')
plt.plot(t, rs, ':', label='rs(t) = sin(2π·8t)')
plt.title("Ejercicio 8: Señales con misma frecuencia, diferente fase")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Correlaciones con referencia seno ----------
R_x1_rs, _ = correlacion_cruzada(x1, rs)
R_x2_rs, _ = correlacion_cruzada(x2, rs)
max_x1_rs = np.max(np.abs(R_x1_rs))
max_x2_rs = np.max(np.abs(R_x2_rs))

# ---------- Correlaciones con referencia coseno ----------
R_x1_rc, _ = correlacion_cruzada(x1, rc)
R_x2_rc, _ = correlacion_cruzada(x2, rc)
max_x1_rc = np.max(np.abs(R_x1_rc))
max_x2_rc = np.max(np.abs(R_x2_rc))

# ---------- Magnitud independiente de fase ----------
mag_x1 = np.sqrt(max_x1_rs**2 + max_x1_rc**2)
mag_x2 = np.sqrt(max_x2_rs**2 + max_x2_rc**2)

# ---------- Resultados ----------
print("=" * 60)
print("Ejercicio 8: Fase y detección sinusoidal")
print("=" * 60)
print(f"{'Par':>20} | {'Máx |Correlación|':>18}")
print("-" * 60)
print(f"{'x1 con seno':>20} | {max_x1_rs:>18.2f}")
print(f"{'x2 con seno':>20} | {max_x2_rs:>18.2f}")
print(f"{'x1 con coseno':>20} | {max_x1_rc:>18.2f}")
print(f"{'x2 con coseno':>20} | {max_x2_rc:>18.2f}")
print("-" * 60)
print(f"{'Magnitud x1':>20} | {mag_x1:>18.2f}")
print(f"{'Magnitud x2':>20} | {mag_x2:>18.2f}")

print("\nInterpretación:")
print("- x1 y rs están en fase → correlación máxima con seno.")
print("- x2 está desfasada π/3 → correlación con seno reducida.")
print("- La magnitud sqrt(R_seno^2 + R_coseno^2) es independiente de la fase.")