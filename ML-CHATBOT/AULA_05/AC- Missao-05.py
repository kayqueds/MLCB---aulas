
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