"""
Exercício 3: O Caminho Perigoso
Cenário: O mesmo corredor do exercício 2, mas agora existe um buraco na posição 2. Se o agente cair no buraco, ele perde 50 pontos e o episódio acaba.
Sua Missão: Adicionar a lógica do buraco, que é uma condição de término negativa.
"""

import numpy as np
import time
# Exercício 3: O Caminho Perigoso
print("\n--- Exercício 3: O Caminho Perigoso ---")
posicao_agente = 5
objetivo = 9
buraco = 2
recompensa_total = 0

# exemplo de loop de passos
for passo in range(15):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")
    
    if acao == 'direita': posicao_agente += 1
    else: posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)

    if posicao_agente == objetivo:
        recompensa_total += 20
        print(" >> Objetivo alcançado!")
        break
    elif posicao_agente == buraco:
        recompensa_total -= 50
        print(" >> Caiu no buraco!")
        break
    else:
        recompensa_total -= 1
    time.sleep(1)
# saída do programa
print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")