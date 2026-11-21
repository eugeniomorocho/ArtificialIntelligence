# Generación de los datos sintéticos de consumo y conexiones.
import numpy as np
import pandas as pd
from itertools import combinations
rng = np.random.default_rng(42)
# Avance de la secuencia para reproducir la referencia original del curso.
rng.standard_normal(1800)
filas = []
for i in range(600):
    particion = "entrenamiento" if i < 300 else (
        "calibracion" if i < 400 else "prueba")
    uso = rng.lognormal(0, .22)
    valores = np.array([120, 70, 4, 2.5, 55, 35]) * uso
    valores += rng.normal(0, [10, 8, .5, .3, 6, 4])
    cambio = particion == "prueba" and i % 10 == 0
    if cambio:
        valores[[0, 1, 4, 5]] *= .15
        valores[[2, 3]] *= 2.5
    filas.append([f"L{i+1:04}", particion,
                  *np.maximum(valores, 0).round(3), int(cambio)])
columnas = ["linea_id", "particion", "min_dia", "min_noche", "gb_dia",
            "gb_noche", "sms_dia", "sms_noche", "cambio_simulado"]
pd.DataFrame(filas, columns=columnas).to_csv("comportamiento_lineas.csv", index=False)
aristas = list(combinations([f"L{i:02d}" for i in range(1, 5)], 2))
aristas += list(combinations([f"L{i:02d}" for i in range(7, 11)], 2))
aristas += [("L04", "L05"), ("L05", "L06"), ("L06", "L07")]
pd.DataFrame(aristas, columns=["origen", "destino"]).to_csv(
    "conexiones_lineas.csv", index=False)
