import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score
df = pd.read_csv("usuarios_app.csv")
assert df.usuario_id.is_unique and not df.isna().any().any()
hora = 2*np.pi*df.hora_central/24
X = np.column_stack([df.frecuencia_apertura, df.funciones_usadas,
                     np.sin(hora), np.cos(hora)])
# Escalamos las cantidades; mantenemos el bloque horario en el círculo unidad.
X[:, :2] = StandardScaler().fit_transform(X[:, :2])
resultados = []
modelos = {}
for k in range(2, 7):
    m = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    resultados.append((k, m.inertia_, silhouette_score(X, m.labels_)))
    modelos[k] = m
tabla = pd.DataFrame(resultados, columns=["k","inercia","silueta"])
print(tabla.to_string(index=False))
k = int(tabla.loc[tabla.silueta.idxmax(), "k"])
df["cluster"] = modelos[k].labels_
print("Candidato por silueta; contrastar con perfiles y propósito:", k)
print(df.groupby("cluster")[["frecuencia_apertura","funciones_usadas"]].agg(["mean","median","count"]))
otra = KMeans(n_clusters=k,n_init=10,random_state=7).fit_predict(X)
print("ARI entre semillas sobre los mismos usuarios:", adjusted_rand_score(df.cluster,otra))
df.to_csv("resultado_segmentacion.csv",index=False)

# Comparación gráfica y perfil horario circular.
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].plot(tabla.k,tabla.inercia,"o-");ax[0].set(xlabel="Número de grupos k",ylabel="Inercia",title="Método del codo")
ax[1].plot(tabla.k,tabla.silueta,"o-");ax[1].set(xlabel="Número de grupos k",ylabel="Silueta",title="Separación y cohesión")
fig.suptitle("Figura P1. Comparación de segmentaciones sintéticas")
fig.text(.5,.01,"Fuente: elaboración propia con usuarios_app.csv y semilla 42.",ha="center",fontsize=8)
fig.tight_layout(rect=(0,.04,1,.93));fig.savefig("comparacion_k.png",dpi=160);plt.close(fig)
for grupo,datos in df.groupby("cluster"):
    angulo=2*np.pi*datos.hora_central.to_numpy()/24
    seno,coseno=np.sin(angulo).mean(),np.cos(angulo).mean()
    concentracion=np.hypot(seno,coseno)
    hora_media=(np.arctan2(seno,coseno)%(2*np.pi))*24/(2*np.pi)
    print(f"Grupo {grupo}: hora circular {hora_media:.2f}, concentración {concentracion:.3f}")
    # Una concentración cercana a cero impediría resumir horarios con una sola hora.


# Complemento breve: K-Means frente a jerárquico con enlace Ward.
from sklearn.cluster import AgglomerativeClustering
etiquetas_ward = AgglomerativeClustering(n_clusters=k, linkage="ward").fit_predict(X)
etiquetas_kmeans = modelos[k].labels_
comparacion = pd.DataFrame([
    {"algoritmo": nombre, "k": len(np.unique(etiquetas)),
     "silueta": silhouette_score(X, etiquetas),
     "tamano_min": int(pd.Series(etiquetas).value_counts().min()),
     "tamano_max": int(pd.Series(etiquetas).value_counts().max())}
    for nombre, etiquetas in [("K-Means", etiquetas_kmeans), ("Jerarquico Ward", etiquetas_ward)]
])
print("Tabla P1. Comparación sobre los mismos 600 usuarios y la misma matriz X")
print(comparacion.round(4).to_string(index=False))
print("Fuente: elaboración propia con usuarios_app.csv; K-Means con semilla 42.")
ari_metodos = adjusted_rand_score(etiquetas_kmeans, etiquetas_ward)
print("ARI entre métodos (acuerdo, no exactitud):", round(ari_metodos, 4))
comparacion.to_csv("resultado_comparacion_algoritmos.csv", index=False)
asignaciones = df[["usuario_id"]].copy()
asignaciones["cluster_kmeans"] = etiquetas_kmeans
asignaciones["cluster_ward"] = etiquetas_ward
asignaciones.to_csv("resultado_asignaciones_algoritmos.csv", index=False)
print("Los identificadores de grupo son arbitrarios y no se comparan por su número.")
