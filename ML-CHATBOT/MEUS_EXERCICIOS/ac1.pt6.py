#Exercicio 6

#numpy serve para trabalhar com arrays e matrizes,facilitando operações matemáticas e manipulação de dados.
#np  é uma abreviação comum para numpy.
#sklearn (ou scikit-learn) é uma biblioteca para machine learning.
#cluster é o módulo dela que trata de agrupamento de dados.
#KMeans é um algoritmo que encontra clusters (grupos) dentro dos seus dados.

import numpy as np 
from sklearn.cluster import KMeans

print("\n--- Exercício Não Supervisionado ---")

#criação de array com dados de produtos (preço, popularidade) com as duas categorias
dados_produtos = np.array([
    [10, 2], [15, 3], [12, 1],   # Categoria 1: Baratos e menos populares
    [200, 9], [180, 8], [210, 10] # Categoria 2: Caros e muito populares
])

# Crie um modelo KMeans para encontrar 2 clusters(TODO)
modelo_produtos = KMeans(n_clusters=2, random_state=42, n_init=10)

# Treine o modelo com os dados dos produtos(TODO)
modelo_produtos.fit(dados_produtos)

# Os centros dos clusters são os nossos produtos "âncora" ideais
produtos_ancora = modelo_produtos.cluster_centers_

print(f"Características dos Produtos Âncora (Preço, Popularidade):\n{produtos_ancora}")
