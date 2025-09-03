# Exercício 01
# bibliotecas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# treinamento supervisionado
print("--- Exercício 1 - Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [nota_prova_1, nota_trabalho_2]
# Rótulos: 0 = Reprovou, 1 = Passou
X_treino = np.array([
    [8, 7], [9, 8], [7, 9], [8, 8],  # Passou
    [4, 5], [3, 4], [5, 3], [4, 4]   # Reprovou
])
y_treino = np.array([1, 1, 1, 1, 0, 0, 0, 0])

# Criando o modelo KNN
modelo_knn = KNeighborsClassifier(n_neighbors=3)
modelo_knn.fit(X_treino, y_treino)

# Testando com novos alunos
aluno_A = np.array([[7, 8]])  # Espera-se que passe (1)
aluno_B = np.array([[4, 3]])  # Espera-se que reprove (0)

# Fazendo previsões
previsao_A = modelo_knn.predict(aluno_A)
previsao_B = modelo_knn.predict(aluno_B)

# minha saída
print(f"Dados de treino (Notas): \n{X_treino}")
print(f"Rótulos de treino (Situação): {y_treino}")
print("-" * 20)
print(f"Previsão para o Aluno A: {'Passou' if previsao_A[0] == 1 else 'Reprovou'}")
print(f"Previsão para o Aluno B: {'Passou' if previsao_B[0] == 1 else 'Reprovou'}")
print("-" * 50, "\n")
