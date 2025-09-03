# Nesta MISSÃO 02 os alunos deverão desenvolver novos algorítmos de Machine Learning em Aprendizado Supervisionado e não supervisionado e um exercício comentando de aprendizdo por reforço.
# VALOR DESTA MISSÃO: 0,25 na AC

# EXEC-01 -  Aprendizado Supervisionado – Aprender com Respostas - "No aprendizado supervisionado, nós damos ao modelo as perguntas (dados) e as respostas (rótulos) e ele precisa aprender a regra que os conecta. Pense em um gabarito de prova."

#Aprendizado Supervisionado (Classificação)
# -------------------------------------------------------------------------
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

print("--- Exercício 1 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [nota_prova_1, nota_trabalho_2]
# Rótulos: 0 = Reprovou, 1 = Passou
# Cloque notas no seu DataSet
X_treino = np.array([
    [, ], [, ], [, ], [, ], # Passou
    [, ], [, ], [, ], [, ]  # Reprovou
])
y_treino = np.array([ ])

# Criando o modelo. O KNN decide o rótulo de um novo ponto olhando para seus vizinhos mais próximos.
# n_neighbors=3 significa que ele vai consultar os 3 vizinhos mais próximos.
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# O '.fit()' é onúcleo do aprendizado: o modelo analisa os dados e ajusta seus parâmetros.
modelo_knn.fit(X_treino, y_treino)

# testar com novos alunos.
aluno_A = np.array([[, ]]) # Esperamos que passe (1)
aluno_B = np.array([[, ]]) # Esperamos que reprove (0)

# O '.predict()' usa o conhecimento adquirido para fazer uma previsão.
previsao_A = modelo_knn.predict(aluno_A)
previsao_B = modelo_knn.predict(aluno_B)

print(f"Dados de treino (Notas): \n{X_treino}")
print(f"Rótulos de treino (Situação): {y_treino}")
print("-" * 20)
print(f"Previsão para o Aluno A: {'Passou' if previsao_A[0] == 1 else 'Reprovou'}")
print(f"Previsão para o Aluno B: {'Passou' if previsao_B[0] == 1 else 'Reprovou'}")
print("-" * 50, "\n")





# EXEC-02 - Aprendizado Supervisionado (Regressão) - Crie um modelo que prevê o preço de um imóvel com base na sua área (m²) e no número de quartos. Usem LinearRegression."
# -----------------------------------------------------------------------
from sklearn.linear_model import LinearRegression

print("--- Exercício 2 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [área_m2, numero_quartos]
# Rótulos: preco_em_milhares_de_reais
X_imoveis = np.array([
    [60, 2], [75, 3], [80, 3], # Imóveis menores
    [120, 3], [150, 4], [200, 4] # Imóveis maiores
])
y_precos = np.array([150, 200, 230, 310, 400, 500])

# TODO: Crie uma instância do modelo LinearRegression.
modelo_regressao = ???

# TODO: Treine o modelo com os dados de imóveis (X_imoveis, y_precos).
???.fit(???, ???)

# TODO: Crie um novo imóvel para testar (ex: 100m², 3 quartos).
imovel_teste = np.array([[100, 3]])

# TODO: Faça a previsão do preço para o novo imóvel.
preco_previsto = ???.predict(???)

# print(f"Previsão de preço para um imóvel de 100m² com 3 quartos: R$ {preco_previsto[0]:.2f} mil")
print("Complete o código acima!")
print("-" * 50, "\n")




# EXEC-03 - Aprendizado Não Supervisionado - Aqui, não temos rótulos, apenas um monte de dados. A tarefa do algoritmo é encontrar padrões, grupos (clusters) por conta própria.
"Vamos usar o algoritmo KMeans para encontrar 2 grupos de clientes com base no valor gasto e na frequência de visitas. Não dizemos qual cliente pertence a qual grupo; o algoritmo deve descobrir."

# Aprendizado Não Supervisionado (Clusterização)
# -----------------------------------------------------------------------------
from sklearn.cluster import KMeans

print("--- Exercício 3 -  Missão 2 (Aprendizado Supervisionado) ---")

# Dados: [valor_gasto_medio, frequencia_visitas_mensal]
# Não temos rótulos!
clientes = np.array([
    [30, 1], [45, 2], [35, 1], # Grupo de baixo valor/frequência
    [500, 8], [600, 10], [550, 9] # Grupo de alto valor/frequência
])

# Criamos o modelo KMeans e pedimos para ele encontrar 2 clusters. Parametrize da forma que seja melhor (ver outros exemplos)
kmeans = KMeans(n_clusters=, random_state=, n_init=)

# '.fit_predict()' treina o modelo e já retorna o cluster de cada cliente.
clusters_encontrados = kmeans.fit_predict(???)

print(f"Dados dos clientes (sem rótulos):\n{clientes}")
print(f"Clusters encontrados pelo KMeans para cada cliente: {clusters_encontrados}")
print("Observe como o algoritmo separou corretamente os clientes nos grupos 0 e 1.")
print("-" * 50, "\n")


# EXEC-04 - Aprendizado Não Supervisionado
"Você é um analista de segurança. Sua missão é identificar transações fraudulentas (anomalias) em um conjunto de dados. Uma transação anômala geralmente está muito distante das outras."
"Use o mesmo KMeans para agrupar as transações. A transação que ficar isolada em seu próprio cluster é provavelmente a anomalia."


print("--- Exercício 4 -  Missão 2 (Aprendizado Não Supervisionado) ---")

# Dados: [valor_transacao, hora_do_dia (0-23)]
transacoes = np.array([
    [15.50, 14], [30.00, 10], [12.75, 11],
    [50.20, 19], [25.00, 9],
    [2500.00, 3] # Uma transação muito alta e de madrugada -> suspeita
])

# TODO: Crie um modelo KMeans para encontrar 2 grupos.
# A ideia é que as transações normais fiquem em um grupo e a anômala fique sozinha no outro.
modelo_anomalia = ???

# TODO: Treine e preveja os clusters para os dados de transações.
clusters_transacoes = ???.fit_predict(???)

# print(f"Clusters para as transações: {clusters_transacoes}")
# print("A transação anômala é aquela que está em um cluster isolado!")
print("Complete o código acima!")
print("-" * 50, "\n")




EXERCICIO FINAL DA MISSÃO 2 - APRENDIZADO POR REFORÇO

Imagine que você está ensinando um Doguinho a buscar um petisco. Você não escreve um manual de instruções para ele. Em vez disso, o processo é interativo:

1 - O cachorro (o Agente) está em um ambiente (a sala). Ele decide fazer uma Ação (andar para frente).
2 - Você dá um Feedback (a Recompensa). Se ele chegou mais perto do petisco, você diz "Bom garoto!" (recompensa positiva).
3 - Se ele foi para longe, você não diz nada (recompensa neutra ou negativa, como o custo de energia).
4 - O cachorro recebe esse feedback e atualiza o seu "entendimento" sobre qual ação é boa naquela situação.
5 - Ele repete esse ciclo de Ação -> Recompensa várias vezes. Depois de muitas tentativas e erros, o cachorro aprende a sequência de ações ideal para conseguir o petisco da forma mais rápida possível.

O Aprendizado por Reforço é exatamente isso: um método de Machine Learning onde um agente aprende a tomar decisões em um ambiente para maximizar uma recompensa total ao longo do tempo.

Exercício: Agente Comilão
Cenário: Nosso agente está em uma linha com 5 posições (0, 1, 2, 3, 4).
O Agente: Um programa que só pode se mover para a 'direita'.
O Ambiente: O caminho de 5 posições.
O Objetivo: Chegar na Comida, que está na posição 4.

Regras de Recompensa:
+20 pontos: Se o agente chegar na Comida.
-1 ponto: Para cada passo que o agente der (representa o custo de energia).

Sua Missão: Você vai preencher a lógica do ambiente. O agente sempre tentará se mover para a 'direita'. Você precisa atualizar a posição dele, verificar se ele alcançou a comida e calcular a recompensa a cada passo.

# ==============================================================================
# EXERCÍCIO 5 - APRENDIZADO POR REFORÇO: O PERSONAGEM COMILÃO
# Objetivo: Entender o loop básico de interação do RL (Ação -> Recompensa).
# ==============================================================================

import time
# --- CONFIGURAÇÃO DO AMBIENTE ---
POSICAO_INICIAL = 0
POSICAO_COMIDA = 4
recompensa_total = 0

# O agente começa na posição inicial.
posicao_agente = POSICAO_INICIAL

print("--- Iniciando a Simulação do PERSONAGEM COMILÃOo ---")
print(f"O agente começa na posição {posicao_agente} e quer chegar na comida na posição {POSICAO_COMIDA}.")
print("-" * 30)

# O agente tem no máximo 10 passos para tentar chegar à comida.
for passo in range(10):
    print(f"Passo {passo + 1}:")
    
# O agente sempre toma a mesma AÇÃO: mover para a 'direita'.
    acao_agente = 'direita'
    print(f"   -> Ação do Agente: '{acao_agente}'")
    
# ======================================================================
# CONSTRUA A LÓGICA DO AMBIENTE
# ======================================================================
    
# 1. ATUALIZE A POSIÇÃO DO AGENTE
#    Se a ação é 'direita', a posição do agente deve aumentar em 1.
     
# 2. CALCULE A RECOMPENSA DO PASSO
#    - Por padrão, a recompensa é -1 (custo de se mover).
#    - MAS, se o agente chegou na POSICAO_COMIDA, a recompensa é +20.
recompensa_do_passo = 0 # Substitua esta linha pela sua lógica.

# 3. ATUALIZE A RECOMPENSA TOTAL
#    Some a recompensa deste passo à 'recompensa_total'.
    
# Exibe o resultado do passo
print(f"   <- Resposta do Ambiente: Nova Posição={posicao_agente}, Recompensa={recompensa_do_passo}")
    
# 4. VERIFIQUE SE O JOGO TERMINOU
#    Se o agente chegou na POSICAO_COMIDA, ele não precisa mais se mover.
#    Use o comando 'break' para parar o loop.
    
# Pausa para visualização
time.sleep(1)

print("-" * 30)
print(f"Simulação Finalizada! Recompensa total acumulada: {recompensa_total}")


# ==============================================================================
# SOLUÇÃO COMENTADA DO EXERCÍCIO
# ==============================================================================

import time
# --- CONFIGURAÇÃO DO AMBIENTE ---
POSICAO_INICIAL = 0
POSICAO_COMIDA = 4
recompensa_total = 0

# O agente começa na posição inicial.
posicao_agente = POSICAO_INICIAL

print("--- Iniciando a Simulação do PERSONAGEM COMILÃO ---")
print(f"O agente começa na posição {posicao_agente} e quer chegar na comida na posição {POSICAO_COMIDA}.")
print("-" * 30)

# O agente tem no máximo 10 passos para tentar chegar à comida.
for passo in range(10):
    print(f"Passo {passo + 1}:")
    
# O agente sempre toma a mesma AÇÃO: mover para a 'direita'.
    acao_agente = 'direita'
    print(f"   -> Ação do Agente: '{acao_agente}'")

# 1. ATUALIZE A POSIÇÃO DO AGENTE
    #    Como a ação é sempre 'direita', simplesmente incrementamos a posição.
    posicao_agente = posicao_agente + 1
        
# 2. CALCULE A RECOMPENSA DO PASSO
#    Verificamos primeiro a condição de vitória.
    if posicao_agente == POSICAO_COMIDA:
        # Se chegou, recebe a recompensa positiva.
        recompensa_do_passo = 20
    else:
        # Se ainda não chegou, recebe a penalidade de movimento.
        recompensa_do_passo = -1

# 3. ATUALIZE A RECOMPENSA TOTAL
#    Acumulamos a recompensa do passo na variável total.
    recompensa_total = recompensa_total + recompensa_do_passo
        
# Exibe o resultado do passo
    print(f"   <- Resposta do Ambiente: Nova Posição={posicao_agente}, Recompensa={recompensa_do_passo}")
        
# 4. VERIFIQUE SE O JOGO TERMINOU
#    Se a condição de vitória foi atingida, paramos a simulação.
    if posicao_agente == POSICAO_COMIDA:
        print("\nO personagem encontrou a comida!")
        break
        
# Pausa para visualização
    time.sleep(1)

print("-" * 30)
print(f"Simulação Finalizada! Recompensa total acumulada: {recompensa_total}")
# Resultado esperado: O agente leva 4 passos, acumulando -4 de recompensa. No 4º passo, ele alcança a comida e ganha +20. Recompensa total: (-1 * 3) + 20 = 17. Não, espera.
# Passo 1: pos=1, rec=-1, total=-1
# Passo 2: pos=2, rec=-1, total=-2
# Passo 3: pos=3, rec=-1, total=-3
# Passo 4: pos=4, rec=+20, total=17
# O resultado esperado é 17.