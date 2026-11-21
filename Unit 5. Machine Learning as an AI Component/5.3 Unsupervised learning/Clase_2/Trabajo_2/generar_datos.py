# Generación de los dos conjuntos sintéticos de la práctica.
import numpy as np
import pandas as pd
plantillas = [
    ("telefonia", "telefono celular smartphone pantalla bateria camara"),
    ("audio", "audifonos auriculares bluetooth sonido microfono"),
    ("computacion", "computador portatil laptop memoria teclado pantalla"),
    ("cocina", "licuadora cocina vaso potencia cuchillas"),
    ("deporte", "zapatillas calzado correr deporte ligero"),
    ("hogar", "lampara escritorio luz lectura regulable")]
filas = []
extras = ["compacto", "recargable", "resistente", "portatil", "nuevo"]
for i in range(120):
    categoria, descripcion = plantillas[i % 6]
    filas.append([f"P{i+1:03}", f"{categoria.capitalize()} modelo {i+1}",
                  categoria, descripcion + " " + extras[i % 5]])
columnas = ["producto_id", "nombre", "categoria", "descripcion"]
pd.DataFrame(filas, columns=columnas).to_csv("catalogo_productos.csv", index=False)
rng = np.random.default_rng(42)
transacciones = pd.DataFrame({
    "transaccion_id": [f"T{i:03d}" for i in range(1, 201)],
    "monto_usd": rng.lognormal(3.6, .45, 200).round(2),
    "compras_24h": rng.poisson(2, 200) + 1,
    "antiguedad_cuenta_dias": rng.integers(30, 1000, 200)})
# Combinaciones extremas didácticas, sin etiquetas de fraude.
transacciones.loc[192:199, "monto_usd"] = np.arange(500, 900, 50)
transacciones.loc[192:199, "compras_24h"] = np.arange(15, 23)
transacciones.loc[192:199, "antiguedad_cuenta_dias"] = np.arange(1, 9)
transacciones.to_csv("transacciones_sinteticas.csv", index=False)
