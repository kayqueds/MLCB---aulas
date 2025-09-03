#numpy importa a biblioteca do machine learning em python
import numpy as np 
from sklearn.cluster import KMeans #skklear importa metodos de clusterizacao e KMeans é usado para separar(clusters)

print("--- Exercício 3 -  Missão 2 (Aprendizado Não Supervisionado) ---")

# Dados: [valor_gasto_medio, frequencia_visitas_mensal]

clientes = np.array([
    [30, 1], [45, 2], [35, 1],   # Grupo de baixo valor/frequência
    [500, 8], [600, 10], [550, 9] # Grupo de alto valor/frequência
])

# Criamos o modelo KMeans e pedimos para ele encontrar 2 clusters
#aqui é criado um objeto kmeans da classe KMeans com os parametros especificados
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
#n_clusters=2 aqui é definido que queremos a divisão em 2 grupos
#random_state=42 é para garantir que o algoritimo sempre comece da mesma forma
#n_init=10 define o número de vezes que o algoritmo será executado com diferentes centroides iniciais no caso 10 vezes

# '.fit_predict()' treina o modelo e já retorna o cluster de cada cliente.
clusters_encontrados = kmeans.fit_predict(clientes)
#o fit separa os dados dos clientes para cada grupo(cluster) e o predict retorna os grupos encontrados

print(f"Dados dos clientes (sem rótulos):\n{clientes}")
print(f"Clusters encontrados pelo KMeans para cada cliente: {clusters_encontrados}")
print("Observe como o algoritmo separou corretamente os clientes nos grupos 0 e 1.")
print("-" * 50, "\n")
