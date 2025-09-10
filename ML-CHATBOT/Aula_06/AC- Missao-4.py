import numpy as np #isso server para importar a biblioteca numpy que é usada para fazer operações matemáticas
#sem essa biblioteca o python não reconhece o np.random.choice e o np.clip
import time #Isso deixa a simulação mais realista/legível, porque você consegue acompanhar o agente andando passo a passo, em vez de rodar tudo de uma vez no terminal.

# Exercício 4: O Chão de Lava
print("\n--- Exercício 4: O Chão de Lava ---")
posicao_agente = 0#posição inicial do agente
objetivo = 9#posição do objetivo
# posições do chão de lava
# o agente perde mais pontos se pisar nessas posições
chao_de_lava = [3, 4, 5]
recompensa_total = 0

for passo in range(20):#máximo de 20 passos que o agente pode dar
    acao = np.random.choice(['esquerda', 'direita'])#escolhe uma ação aleatória entre esquerda e direita
    print(f"Passo {passo + 1}: Posição={posicao_agente}, Ação='{acao}'")

    # aqui se a açao escolhida for direira a posição do agente aumenta 1 se for esquerda diminui 1
    # o np.clip serve para limitar a posição do agente entre 0 e 9 não deixando ele sair do ambiente
    if acao == 'direita':
        posicao_agente += 1
    else:
        posicao_agente -= 1
    posicao_agente = np.clip(posicao_agente, 0, 9)


#aqui é usado if e else para atribuir valores para a a ariavel recompensa_passo(pontuação atual)
#ou seja se o agente pisar no chão de lava ele perde 5 pontos
#se ele pisar no chão normal ele perde 1 ponto
#se o agente chegar no objetivo ele ganha 50 pontos
    # TODO 1: Chegou no objetivo?
    if posicao_agente == objetivo:
        recompensa_total += 50
        print("🎯 Objetivo alcançado! +50 pontos")
        break

    # TODO 2: Recompensa do passo
    if posicao_agente in chao_de_lava:
        recompensa_passo = -5
        print("🔥 Chão de lava! -5 pontos")
    else:
        recompensa_passo = -1
        print("🟩 Chão normal -1 ponto")

    # TODO 3: Soma recompensa
    recompensa_total += recompensa_passo#atualiza a pontuação total do agente

    time.sleep(0.5)#com o sleep é possível ver o agente andando passo a passo sem ele a simulação roda tudo de uma vez no terminal

print(f"Simulação finalizada! Posição final: {posicao_agente}, Recompensa: {recompensa_total}")
