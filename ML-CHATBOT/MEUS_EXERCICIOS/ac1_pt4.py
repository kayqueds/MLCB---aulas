# TAREFA 4 :Treine o modelo abaixo colocando mais 3 conjuntos de dados e parametrize para 3 clusters e rode sem erros no VSCODE - Faça teste após o treinamento 
# aprendizado não supervisionado para agrupar mensagens semelhantes sem informar ao modelo quais são suas categorias.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


# 1. Matriz de mensagens (sem rótulos)
mensagens = [
    "Quero pedir pizza",
    "Qual o valor da pizza grande?",
    "Preciso de suporte no aplicativo",
    "O app está travando",
    "Vocês têm sobremesas?",
    "Meu pedido está atrasado",
    "Como faço para cancelar meu pedido?",  
    "Qual o horário de funcionamento?",    
    "O pagamento não foi aprovado"         
]

# 2. Vetorizar texto
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(mensagens)

# 3. Criar modelo de agrupamento com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# 4. Interação: classificar nova frase
while True:
    nova_mensagem = input("\nDigite uma nova mensagem (ou 'sair' para encerrar): ")
    if nova_mensagem.lower() == "sair":
        break
    X_novo = vectorizer.transform([nova_mensagem])
    cluster_previsto = kmeans.predict(X_novo)
    print(f"Essa mensagem se parece com o Cluster {cluster_previsto[0]}")

