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


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("catalogo_productos.csv")
assert df.producto_id.is_unique and df.descripcion.notna().all()
vectorizador = TfidfVectorizer(lowercase=True,strip_accents="unicode",ngram_range=(1,2))
X = vectorizador.fit_transform(df.descripcion)
S = cosine_similarity(X)
no_nulos = np.asarray(X.getnnz(axis=1)).ravel() > 0
assert np.allclose(np.diag(S)[no_nulos],1.0,atol=1e-10)
def recomendar(idx,k=3):
    puntajes = S[idx].copy()
    puntajes[idx] = -np.inf  # Excluir por índice, incluso si hay empates.
    orden = np.argsort(-puntajes,kind="stable")[:k]
    resultado = df.iloc[orden][["producto_id","nombre","categoria","descripcion"]].copy()
    resultado["similitud"] = puntajes[orden]
    return resultado
for idx in [0,1]:
    print("Consulta:",df.iloc[idx]["nombre"])
    print(recomendar(idx).to_string(index=False))
consulta = vectorizador.transform(["auriculares para escuchar musica"])
print("Consulta sin términos conocidos:",consulta.nnz==0)
print("Nota: coincidencia textual no demuestra relevancia para usuarios reales.")

# Contraste básico con unigramas sobre las mismas consultas.
vectorizador_uni=TfidfVectorizer(lowercase=True,strip_accents="unicode")
U=vectorizador_uni.fit_transform(df.descripcion)
Su=cosine_similarity(U)
for idx in [0,1]:
    puntajes=Su[idx].copy();puntajes[idx]=-np.inf
    top=np.argsort(-puntajes,kind="stable")[:3]
    print("Unigramas, consulta",df.iloc[idx].producto_id,":",list(df.iloc[top].producto_id))
# Demostración explícita de consulta fuera del vocabulario.
assert vectorizador.transform(["xyzterminodesconocido"]).nnz==0
print("Consulta vacía o fuera del vocabulario: no se presentan resultados como relevantes.")


# Complemento breve: Isolation Forest sobre tres variables numéricas.
from sklearn.ensemble import IsolationForest
transacciones = pd.read_csv("transacciones_sinteticas.csv")
variables_if = ["monto_usd", "compras_24h", "antiguedad_cuenta_dias"]
assert transacciones.transaccion_id.is_unique
assert not transacciones[variables_if].isna().any().any()
# Exploración descriptiva de un lote, sin evaluación de generalización ni etiquetas.
X_if = transacciones[variables_if]
modelo_if = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
modelo_if.fit(X_if)
resultado_if = transacciones.copy()
# score_samples es menor para casos más anómalos; cambiamos el signo al presentar.
resultado_if["puntaje_anomalia"] = -modelo_if.score_samples(X_if)
resultado_if["alerta"] = modelo_if.predict(X_if) == -1
resultado_if = resultado_if.sort_values("puntaje_anomalia", ascending=False, kind="stable")
print("Tabla P2. Cinco transacciones con mayor puntuación de anomalía")
print(resultado_if.head(5).round(4).to_string(index=False))
print("Fuente: elaboración propia con transacciones_sinteticas.csv; semilla 42.")
print("Observaciones:", len(resultado_if), "Alertas:", int(resultado_if.alerta.sum()))
print("Referencia del lote (medianas):", X_if.median().to_dict())
print("contamination=0.05 fija un umbral didáctico; no estima la proporción de fraude.")
print("Las alertas requieren revisión. Sin casos confirmados no se calcula exactitud.")
resultado_if.to_csv("resultado_isolation_forest.csv", index=False)
