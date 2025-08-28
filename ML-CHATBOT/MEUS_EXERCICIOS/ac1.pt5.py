#Exercicio 5

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

#criação do vetor com as frases de turismo
frases = [
    "Quero comprar uma passagem para o Rio de Janeiro",
    "Preciso reservar um hotel em São Paulo",
    "Gostaria de conhecer pontos turísticos em Salvador",
    "Quero dicas de restaurantes em Florianópolis",
    "Qual o preço da passagem para Recife?",
    "Existe hostel barato em Belo Horizonte?",
    "Quais passeios você recomenda em Foz do Iguaçu?",
    "Onde posso jantar bem em Curitiba?",
    "Quero reservar passagem de avião para Brasília",
    "Procuro pousada perto da praia em Fortaleza",
    "Tem algum passeio de barco em Manaus?",
    "Me indique uma churrascaria em Porto Alegre"
]

# 2. Vetorização

 # aqui é criada uma variavel que guarda oobjeto CountVectorizer que transforma as frases em vetores contando as palavras
vectorizer = CountVectorizer()
#aqui as frases são transformadas em uma matriz números resultante da vetorização das frases.
#fit: aprende o vocabulário de todas as frases (todas as palavras únicas).
#transform: converte cada frase em um vetor numérico, onde cada posição corresponde a uma palavra do vocabulário e o valor é a quantidade de vezes que a palavra aparece naquela frase.
X = vectorizer.fit_transform(frases)

# 3. Modelo KMeans (definindo 4 clusters: passagens, hospedagem, passeios, restaurantes)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)# aqui é criada uma variavel no kmeans para definir o numero de clusters(n_clusters)
#que os resultados serão sempre iguais(random_state=42) e o n_init define quantas vezes o algoritmo será executado com diferentes centroides iniciais
kmeans.fit(X)# aqui as frases vão ser organizados nos 4 clusters

# 4. Saída: mostrar cluster de cada frase kmeans.labels_ puxa o numero do cluster de cada frase
for frase, cluster in zip(frases, kmeans.labels_):
    print(f"Cluster {cluster}: {frase}")