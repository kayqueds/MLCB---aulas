import numpy as np
import time

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
    bateria -= 10
    
    # TODO 2: Verifique as condições de término.
    if posicao_agente == objetivo:
        recompensa_total +=50
        print("Agente chegou ao objetivo! Recompensa +50")
        break
    elif bateria <= 0:
        print("Bateria esgotada! Episódio terminado")
        break
    else:
        pass # Continua o episódio
    
    time.sleep(0.5)
    
print(f"Simulação finalizada! Posição: {posicao_agente}, Bateria: {bateria}%, Recompensa: {recompensa_total}")
