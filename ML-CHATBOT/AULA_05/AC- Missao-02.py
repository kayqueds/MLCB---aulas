# Instaalando as bibliotecas
from sklearn.linear_model import LinearRegression
import numpy as np

print("--- Exercício 2 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [área_m2, numero_quartos]
# Rótulos: preco_em_milhares_de_reais
X_imoveis = np.array([
    [60, 2], [75, 3], [80, 3], # Imóveis menores
    [120, 3], [150, 4], [200, 4] # Imóveis maiores
])
y_precos = np.array([150, 200, 230, 310, 400, 500])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_regressao = LinearRegression()

# TODO: Treine o modelo com os dados de imóveis (X_imoveis, y_precos).
modelo_regressao.fit(X_imoveis, y_precos)

# TODO: Crie um novo imóvel para testar (ex: 100m², 3 quartos).
imovel_teste = np.array([[100, 3]])

# TODO: Faça a previsão do preço para o novo imóvel.
preco_previsto = modelo_regressao.predict(imovel_teste)

# print(f"Previsão de preço para um imóvel de 100m² com 3 quartos: R$ {preco_previsto[0]:.2f} mil")
print(f"previção de preço para um imóvel de 100m² com 3 quartos: R$ {preco_previsto[0]:.2f} mil")
print("-" * 50, "\n")