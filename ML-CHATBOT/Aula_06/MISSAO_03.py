Cada exercício foca em um conceito fundamental do design de ambientes de RL.
Eles são projetados para serem resolvidos em sequência, construindo o conhecimento passo a passo.
O objetivo é que os alunos implementem a lógica do ambiente, que é o primeiro passo para dominar o RL.

Instruções para os Alunos
Para cada exercício, você receberá um cenário e um código-fonte com seções marcadas como # TODO.
Sua missão é preencher essas seções para que a simulação funcione de acordo com as regras descritas.
No final de cada exercício, a solução completa é fornecida para sua referência.

Exercício Introdutório: Identificando os Componentes de RL em um Novo Cenário
Objetivo: Consolidar a compreensão dos conceitos fundamentais do Aprendizado por Reforço (Agente, Ambiente, Estado, Ação, Recompensa, Política e Função de Valor) em um contexto diferente do labirinto.
Cenário:Imagine que você está construindo um sistema de IA para ensinar um robô-aspirador a limpar eficientemente uma casa. O robô se move em diferentes cômodos, encontra sujeira e, eventualmente, precisa retornar à sua base para recarregar.
Tarefa:Para este cenário do robô-aspirador, identifique e descreva cada um dos seguintes componentes de Aprendizado por Reforço:
Agente:
Ambiente:
Estado (exemplifique alguns estados possíveis):
Ação (exemplifique algumas ações possíveis):
Recompensa (sugira algumas recompensas positivas e negativas):
Política (descreva brevemente o que uma política representaria aqui):
Função de Valor Q (o que ela tentaria estimar neste contexto?):


EXERCICIOS PADRÕES
Setup Inicial (para todos os exercícios):
Crie um arquivo Python e instale a biblioteca NumPy:
pip install numpy

---

### **Exercício 1: O Corredor Simples**

**Cenário:** O exercício mais básico possível. Um agente está em um corredor de 7 posições (0 a 6) e quer chegar ao final. Ele só pode se mover para frente.

**Sua Missão:** Implementar a lógica de movimento e a recompensa final.

```python
# Exercício 1: O Corredor Simples
import numpy as np
import time

print("\n--- Exercício 1: O Corredor Simples ---")
posicao_agente = 0
objetivo = 6
recompensa_total = 0

for passo in range(10):
    print(f"Passo {passo + 1}: Posição atual = {posicao_agente}")
    
    # Neste cenário simples, a única ação possível é 'avançar'.
    # TODO 1: Atualize a 'posicao_agente' para que ele avance 1 passo.
    
    
    # TODO 2: Verifique se o agente alcançou o 'objetivo'.
    # Se sim, adicione 10 pontos à 'recompensa_total' e use 'break' para parar.
    
    
    # Se não chegou, ele perde 1 ponto de 'recompensa_total' pelo esforço.
    
    
    time.sleep(0.5)

print(f"Simulação finalizada! Recompensa total: {recompensa_total}")

Solução do Exercício 1:
# --- Solução Exercício 1 ---
# print("\n--- Solução Exercício 1 ---")
# posicao_agente = 0
# objetivo = 6
# recompensa_total = 0
# for passo in range(10):
#     print(f"Passo {passo + 1}: Posição atual = {posicao_agente}")
#     # TODO 1: Atualize a 'posicao_agente' para que ele avance 1 passo.
#     posicao_agente += 1
#
#     # TODO 2: Verifique se o agente alcançou o 'objetivo'.
#     if posicao_agente == objetivo:
#         print(" >> Objetivo alcançado!")
#         recompensa_total += 10
#         break
#     else:
#         # Se não chegou, ele perde 1 ponto de 'recompensa_total' pelo esforço.
#         recompensa_total -= 1
#     time.sleep(0.5)
# print(f"Simulação finalizada! Recompensa total: {recompensa_total}") # Resultado esperado: 4
Exercício 2: O Agente Indeciso
Cenário: Agora o agente pode se mover para 'esquerda' ou 'direita' em um corredor de 10 posições (0 a 9). Ele não pode atravessar as paredes (posições < 0 ou > 9).
Sua Missão: Implementar a lógica de movimento para ambas as direções e garantir que o agente permaneça dentro dos limites do corredor.





# Exercício 2: O Agente Indeciso
print("\n--- Exercício 2: O Agente Indeciso ---")
posicao_agente = 5
objetivo = 9
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    # TODO 1: Crie uma estrutura if/elif para atualizar a 'posicao_agente'.
    # Se a ação for 'direita', some 1. Se for 'esquerda', subtraia 1.
    
    
    # TODO 2: Garanta que o agente não saia dos limites (0 e 9).
    # Use as funções max() e min() para isso. Ex: posicao = max(0, posicao)
    
    
    # TODO 3: Se o agente chegar no 'objetivo', dê +20 de recompensa e pare (break).
    # Senão, ele perde 1 ponto de recompensa.
    
    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")



Exercício 3: O Caminho Perigoso
Cenário: O mesmo corredor do exercício 2, mas agora existe um buraco na posição 2. Se o agente cair no buraco, ele perde 50 pontos e o episódio acaba.
Sua Missão: Adicionar a lógica do buraco, que é uma condição de término negativa.

# Exercício 3: O Caminho Perigoso
print("\n--- Exercício 3: O Caminho Perigoso ---")
posicao_agente = 5
objetivo = 9
buraco = 2
recompensa_total = 0

for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9) # np.clip faz o mesmo que max/min

    # TODO 1: Crie uma estrutura if/elif/else para as recompensas.
    # - Se a posição for igual ao 'objetivo': recompensa +20, fim.
    # - Se a posição for igual ao 'buraco': recompensa -50, fim.
    # - Senão: recompensa -1.
    
    
    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")

Exercício 4: O Chão de Lava
Cenário: Algumas posições no corredor são "quentes" (chão de lava) e dão uma penalidade maior ao agente.
Sua Missão: Implementar uma recompensa de passo que depende do estado (posição) do agente.

# Exercício 4: O Chão de Lava
print("\n--- Exercício 4: O Chão de Lava ---")
posicao_agente = 0
objetivo = 9
chao_de_lava = [3, 4, 5]
recompensa_total = 0

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")

    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)

    # TODO 1: Verifique se o agente chegou no 'objetivo'. Se sim, recompensa +50 e fim.
    
    
    # TODO 2: Crie uma variável 'recompensa_passo'.
    # - Se a 'posicao_agente' estiver na lista 'chao_de_lava', a recompensa do passo é -5.
    # - Senão, a recompensa do passo é -1 (chão normal).
    
    
    # TODO 3: Adicione a 'recompensa_passo' à 'recompensa_total'.
    
    
    time.sleep(0.5)

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")

Exercício 5: O Robô com Bateria
Cenário: O agente agora é um robô com uma bateria que começa em 100%. Cada passo consome 10% da bateria. Se a bateria chegar a 0, o episódio acaba.
Sua Missão: Adicionar e gerenciar um segundo componente do estado: a energia.

# Exercício 5: O Robô com Bateria
print("\n--- Exercício 5: O Robô com Bateria ---")
posicao_agente = 0
objetivo = 9
recompensa_total = 0
bateria = 100 # Novo estado!

for passo in range(20):
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Bateria={bateria}%")
    
    acao = np.random.choice(['esquerda', 'direita'])
    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)

    # TODO 1: Subtraia 10 da 'bateria' a cada passo.
    
    
    # TODO 2: Verifique as condições de término.
    # - Se chegar no 'objetivo', recompensa +100 e fim.
    # - Se a 'bateria' for menor ou igual a 0, recompensa -30 e fim.
    # - Senão, recompensa do passo é 0 (a penalidade está no gasto da bateria).
    
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição: {posicao_agente}, Bateria: {bateria}%, Recompensa: {recompensa_total}")


### **Exercício 6: O Vento Traiçoeiro**

**Cenário:** O ambiente agora é estocástico (imprevisível). Há uma chance de 30% de que a ação do agente falhe por causa de um "vento forte". Se a ação falhar, o agente não se move, mas ainda paga o custo de -1 ponto.
**Sua Missão:** Introduzir a aleatoriedade do ambiente na lógica de transição de estado.

# Exercício 6: O Vento Traiçoeiro
print("\n--- Exercício 6: O Vento Traiçoeiro ---")
posicao_agente = 0
objetivo = 9
recompensa_total = 0

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Tentando ir para '{acao}'")
    
    # TODO 1: Use np.random.rand() para simular a chance do vento.
    # np.random.rand() retorna um número entre 0.0 e 1.0.
    # Se o número for menor que 0.3 (30%), a ação falha.
    vento_soprou = np.random.rand() < 0.3
    
    # TODO 2: Crie um if/else baseado em 'vento_soprou'.
    # - Se o vento NÃO soprou, mova o agente normalmente.
    # - Se o vento soprou, o agente NÃO se move.
    
    
    # TODO 3: A recompensa é sempre -1, a menos que o objetivo seja alcançado (+50).
    # Verifique a posição FINAL do agente no passo para decidir a recompensa.
    
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")