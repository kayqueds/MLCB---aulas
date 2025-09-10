# Exercício 6: O Vento Traiçoeiro
print("\n--- Exercício 6: O Vento Traiçoeiro ---")
posicao_agente = 0
objetivo = 9
recompensa_total = 0

import numpy as np
import time

for passo in range(20):
    acao = np.random.choice(['esquerda', 'direita'])
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Tentando ir para '{acao}'")
    
    # TODO 1: Use np.random.rand() para simular a chance do vento.
    # np.random.rand() retorna um número entre 0.0 e 1.0.
    # Se o número for menor que 0.3 (30%), a ação falha.
    vento_soprou = np.random.rand() < 0.3
    if not vento_soprou:
        if acao == 'direita':
            posicao_agente += 1
        else:
            posicao_agente -= 1
        posicao_agente = np.clip(posicao_agente, 0, 9)

    # TODO 2: Crie um if/else baseado em 'vento_soprou'.
    # - Se o vento NÃO soprou, mova o agente normalmente.
    # - Se o vento soprou, o agente NÃO se move.
    if vento_soprou:
        print(" >> O vento soprou! Ação falhou.")
    else:
        print(" >> Ação bem-sucedida.")

    
    # TODO 3: A recompensa é sempre -1, a menos que o objetivo seja alcançado (+50).
    # Verifique a posição FINAL do agente no passo para decidir a recompensa.
    
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")