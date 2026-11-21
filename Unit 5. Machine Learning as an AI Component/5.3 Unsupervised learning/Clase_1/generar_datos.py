# Generación de los datos sintéticos de la práctica.
import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
filas = []
for i in range(600):
    g = i % 3
    frecuencia = max(1, int(rng.normal([6, 22, 45][g], [2, 6, 9][g])))
    funciones = int(np.clip(round(rng.normal([2, 4, 6][g], 1)), 1, 8))
    hora = float(rng.normal([8, 14, 21][g], 2) % 24)
    filas.append([f"U{i+1:04}", frecuencia, funciones, round(hora, 2)])
columnas = ["usuario_id", "frecuencia_apertura", "funciones_usadas", "hora_central"]
pd.DataFrame(filas, columns=columnas).to_csv("usuarios_app.csv", index=False)
