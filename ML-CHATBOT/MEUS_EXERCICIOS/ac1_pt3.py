# Exercicio 03

import numpy as np
from sklearn.linear_model import LinearRegression

print("\n--- 1.2 Exercício para Alunos (Supervisionado) ---")

dados_entregas = np.array([
    [5, 2],   # 5 km, 2 pizzas
    [2, 1],   # 2 km, 1 pizza
    [10, 4],  # 10 km, 4 pizzas
    [7, 3],   # 7 km, 3 pizzas
    [1, 1]    # 1 km, 1 pizza
])

tempos_entrega = np.array([30, 15, 55, 40, 10])

modelo_entrega = LinearRegression ()

modelo_entrega.fit(dados_entregas, tempos_entrega)


pedido_novo = np.array([[1, 2]])
tempo_previsto = modelo_entrega.predict(pedido_novo)

print(f"Tempo de entrega previsto para o novo pedido: {tempo_previsto[0]:.2f} minutos")