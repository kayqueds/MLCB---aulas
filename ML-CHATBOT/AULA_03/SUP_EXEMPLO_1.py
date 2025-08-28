# Para instalar as bibliotecas, abra o terminal e digite:
# pip install scikit-learn numpy
# ==============================================================================

import numpy as np

# ==============================================================================
#APRENDIZADO SUPERVISIONADO
# Conceito: O algoritmo aprende de um conjunto de dados que contém as "respostas certas" (rótulos).
# Analogia: Aprender para uma prova usando um livro com gabarito.
# ==============================================================================
# Exemplo: Classificação de Frutas
# Problema: Prever se uma fruta é uma Maçã ou uma Laranja com base no seu peso e textura.
# ------------------------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier

print("\n--- Exemplo Supervisionado ---")

# Dados de Treino:
# Característica 1: Peso em gramas
# Característica 2: Textura (0 para Lisa, 1 para Cascuda/Irregular)
# Formato: [peso, textura]
dados_frutas = np.array([
    [150, 0], [170, 0], # Maçãs (lisas)
    [140, 1], [130, 1]  # Laranjas (cascudas)
])

# Rótulos (Labels): As respostas corretas que o algoritmo deve aprender.
# 0 = Laranja, 1 = Maçã
rotulos_frutas = np.array([1, 1, 0, 0])

# Criando o modelo de classificação (K-Nearest Neighbors). Ele classifica um novo dado com base nos seus 'k' vizinhos mais próximos.
modelo_frutas = KNeighborsClassifier(n_neighbors=1)

# Treinando o modelo: O comando .fit() é onde o aprendizado acontece.
modelo_frutas.fit(dados_frutas, rotulos_frutas)

# Fazendo previsão para uma nova fruta misteriosa.
# Ex: Uma fruta com 160g e textura lisa (0).
fruta_misteriosa = np.array([[160, 0]])
previsao = modelo_frutas.predict(fruta_misteriosa)

resultado = "Maçã" if previsao[0] == 1 else "Laranja"
print(f"A fruta misteriosa de [160g, Lisa] foi classificada como: {resultado}")
