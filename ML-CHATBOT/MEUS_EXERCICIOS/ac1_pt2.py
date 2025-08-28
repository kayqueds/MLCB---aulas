#### TAREFA 2 :  Criar um classificador de mensagens para um bot de atendimento acadêmico - rode sem erros no VSCODE ###

# Criar um classificador de mensagens para um bot de atendimento acadêmico.
# Instruções:
# 1. Crie uma lista de frases (ex: dúvidas sobre matrícula, notas, eventos, biblioteca)
# 2. Crie a lista de rótulos correspondentes
# 3. Vetorize as frases com CountVectorizer
# 4. Treine um modelo Naive Bayes ou outro de sua escolha
# 5. Teste com uma nova frase e imprima o resultado

# início código
# 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Dataset
frases = [
    "Como é feito o pagamento da matrícula?",''
    "Como é feito a somatória das notas?",
    "Quais são os eventos programados para este semestre?",
    "Como faço para acessar a biblioteca?"
]
rotulos = [
    "matricula",
    "notas",
    "eventos",
    "biblioteca"
]

# 2. Vetorização
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

# 3. Modelo
modelo = MultinomialNB()
modelo.fit(X, rotulos)

# 4. Previsão
nova_frase = ["Como é feito a somatória das notas?"]
X_nova = vectorizer.transform(nova_frase)
previsao = modelo.predict(X_nova)
print(previsao)

