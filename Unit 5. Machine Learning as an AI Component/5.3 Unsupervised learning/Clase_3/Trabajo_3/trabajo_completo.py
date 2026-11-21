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


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.decomposition import PCA
df = pd.read_csv("comportamiento_lineas.csv")
variables = ["min_dia","min_noche","gb_dia","gb_noche","sms_dia","sms_noche"]
tr = df.particion.eq("entrenamiento")
cal = df.particion.eq("calibracion")
te = df.particion.eq("prueba")
escalador = StandardScaler().fit(df.loc[tr,variables])
Xtr = escalador.transform(df.loc[tr,variables])
Xcal = escalador.transform(df.loc[cal,variables])
Xte = escalador.transform(df.loc[te,variables])
ae = MLPRegressor(hidden_layer_sizes=(3,),activation="tanh",solver="lbfgs",
                  max_iter=2000,random_state=42,alpha=.01)
ae.fit(Xtr,Xtr)
error_cal = np.mean((Xcal-ae.predict(Xcal))**2,axis=1)
umbral = np.quantile(error_cal,.95)
error_te = np.mean((Xte-ae.predict(Xte))**2,axis=1)
resultado = df.loc[te,["linea_id","cambio_simulado"]].copy()
resultado["error_reconstruccion"] = error_te
resultado["alerta"] = error_te > umbral
print("Umbral de calibración:",umbral)
print(resultado.sort_values("error_reconstruccion",ascending=False).head(20).to_string(index=False))
# La etiqueta simulada nunca entró al entrenamiento ni a la calibración.
print(pd.crosstab(resultado.cambio_simulado,resultado.alerta))
pca=PCA(n_components=3).fit(Xtr)
error_pca=np.mean((Xte-pca.inverse_transform(pca.transform(Xte)))**2)
print("MSE prueba, PCA:",error_pca,"AE:",error_te.mean())
print("Estas alertas detectan desviaciones de la referencia; no predicen cancelaciones.")
resultado.to_csv("resultado_alertas.csv",index=False)

# Evidencia separada para calibración y prueba.
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,4))
ax.hist(error_cal,bins=25,alpha=.6,label="Calibración")
ax.hist(error_te,bins=25,alpha=.6,label="Prueba")
ax.axvline(umbral,color="black",linestyle="--",label="Percentil 95 de calibración")
ax.set(xlabel="Error cuadrático medio por observación",ylabel="Observaciones",title="Figura P1. Errores de reconstrucción")
ax.legend();fig.text(.5,.01,"Fuente: elaboración propia con comportamiento_lineas.csv; autoencoder 6–3–6.",ha="center",fontsize=8)
fig.tight_layout(rect=(0,.05,1,1));fig.savefig("errores_reconstruccion.png",dpi=160);plt.close(fig)
print("Filas por partición:",df.particion.value_counts().to_dict())
print("Resumen por partición:\n",df.groupby("particion")[variables].agg(["mean","std"]))
for estado in [True,False]:
    print("Ejemplo con alerta =",estado)
    print(resultado[resultado.alerta.eq(estado)].head(1).to_string(index=False))


# Complemento breve: grafo simple, no dirigido y sin pesos.
import networkx as nx
aristas = pd.read_csv("conexiones_lineas.csv")
assert not aristas.isna().any().any()
assert not aristas.origen.eq(aristas.destino).any()
G = nx.from_pandas_edgelist(aristas, source="origen", target="destino", create_using=nx.Graph())
assert G.number_of_nodes() == 10 and G.number_of_edges() == 15
centralidad_grado = nx.degree_centrality(G)
centralidad_intermediacion = nx.betweenness_centrality(G, normalized=True, weight=None)
centralidades = pd.DataFrame({"nodo": sorted(G.nodes)})
centralidades["grado"] = centralidades.nodo.map(dict(G.degree()))
centralidades["centralidad_grado"] = centralidades.nodo.map(centralidad_grado)
centralidades["intermediacion"] = centralidades.nodo.map(centralidad_intermediacion)
centralidades = centralidades.sort_values(["intermediacion", "nodo"], ascending=[False, True])
print("Tabla P3. Centralidades del grafo sintético")
print(centralidades.round(4).to_string(index=False))
print("Fuente: elaboración propia con conexiones_lineas.csv y NetworkX.")
print("Nodos:", G.number_of_nodes(), "Aristas:", G.number_of_edges())
centralidades.to_csv("resultado_centralidades.csv", index=False)
fig, ax = plt.subplots(figsize=(8, 4.8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, ax=ax, node_color="#e8edf2", edgecolors="#273746",
                 edge_color="#708090", node_size=1000, font_size=10, width=1.4)
ax.set_title("Figura P2. Conexiones sintéticas entre diez líneas")
ax.set_axis_off()
fig.text(.5, .025, "Fuente: elaboración propia con conexiones_lineas.csv; diseño de red con semilla 42.", ha="center", fontsize=8)
fig.tight_layout(rect=(0, .05, 1, 1))
fig.savefig("grafo_lineas.png", dpi=160)
plt.close(fig)
print("Cada arista representa una conexión simulada; se omiten dirección y frecuencia.")
print("Las centralidades describen esta red; no demuestran influencia comercial ni fraude.")
