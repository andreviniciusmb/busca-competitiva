import random
import time

humano = 'O' ## Marcador do jogador huamno
pc = 'X'     ## Marcador do jogador PC
vazio = ' '  ## Marcador do estado vazio

def jogada_humano(tabuleiro):
    '''
    Retorna o tabuleiro atualizado com a jogada do humano
    @param Tabuleiro
    '''
    exibe_tabuleiro(tabuleiro)
    print("\n> Selecione sua jogada...")
    linha = -10
    coluna = -10
    aux = False ## Variável auxiliar para ver se a posição escolhida está vazia
    while not(aux):
        while (linha <= -1) | (linha >= 3):
            print(">> Linha [0,1,2]:")
            linha = int(input())
        while (coluna <= -1) | (coluna >= 3):
            print(">> Coluna [0,1,2]:")
            coluna = int(input())
        if tabuleiro[linha][coluna] == vazio:
            tabuleiro[linha][coluna] = humano
            aux = True
        else:
            print('>> Jogada invalida!!!')
            aux = False
            linha = -10
            coluna = -10
    
    print('Linha: ' + str(linha) + ' - Coluna: ' + str(coluna))

def final(tabuleiro):
    '''
    Retorna True se o jogo acabou, False caso contrário
    @param Tabuleiro
    @return True/False
    '''
    aux = True
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                aux = False
    
    return aux

def resultado(tabuleiro, linha,coluna):
    '''
    Retorna e exibe o tabuleiro que resulta ao fazer a jogada i,j
    @param Tabuleiro
    '''
    exibe_tabuleiro(tabuleiro)
    tabuleiro[linha][coluna] = 'X'
    print('\n- Tabuleiro atualizado com a última jogada\n')
    print('Linha: ' + str(linha) + ' - Coluna: ' + str(coluna))
    exibe_tabuleiro(tabuleiro)

def ganhador(tabuleiro):
    '''
    Retorna o ganhador do jogo se houver
    @param Tabuleiro do jogo
    @return 0/1/2
    '''
    for linha in range(3):
        if ((tabuleiro[linha][0] == tabuleiro[linha][1]) and (tabuleiro[linha][1] == tabuleiro[linha][2])):
            if tabuleiro[linha][0] == pc:
                return 0
            elif tabuleiro[linha][0] == humano:
                return 1
    
    for coluna in range(3):
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna])):
            if tabuleiro[0][coluna] == pc:
                return 0
            elif tabuleiro[0][coluna] == humano:
                return 1

    if ((tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2])):
            if tabuleiro[0][0] == pc:
                return 0
            elif tabuleiro[0][0] == humano:
                return 1
    
    if ((tabuleiro[2][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[0][2])):
            if tabuleiro[2][0] == pc:
                return 0
            elif tabuleiro[2][0] == humano:
                return 1

    return 2

def custo(tabuleiro):
    '''
    Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
    @param Tabuleiro do jogo
    @return Custo da jogada
    '''
    for linha in range(3):
        if ((tabuleiro[linha][0] == tabuleiro[linha][1]) and (tabuleiro[linha][1] == tabuleiro[linha][2])):
            if tabuleiro[linha][0] == pc:
                return 1
            elif tabuleiro[linha][0] == humano:
                return -1
    
    for coluna in range(3):
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna])):
            if tabuleiro[0][coluna] == pc:
                return 1
            elif tabuleiro[0][coluna] == humano:
                return -1

    if ((tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2])):
            if tabuleiro[0][0] == pc:
                return 1
            elif tabuleiro[0][0] == humano:
                return -1
    
    if ((tabuleiro[2][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[0][2])):
            if tabuleiro[2][0] == pc:
                return 1
            elif tabuleiro[2][0] == humano:
                return -1

    return 0

def acoes(tabuleiro):
    '''
    Retorna todas as jogadas disponíveis
    @param Tabuleiro
    @return Lista de jogadas
    '''
    jogadas = []

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                jogadas.append([i,j])
    return jogadas

def minimax(tabuleiro,altura,ehPC):
    '''
    Retorna a jogada ótima para o jogador atual baseado no algoritmo de minimax
    @param Tabuleiro,altura da árvore, se a pontuação é máxima ou não
    @return Pontuação da jogada.
    '''
    if ((altura < 1) or (final(tabuleiro))):
        pontos = custo(tabuleiro)
        return [-1,-1,pontos]
    
    if ehPC:
        melhor_pontuacao = [-1,-1,-10]

        for espacos_vazios in acoes(tabuleiro):
            i,j = espacos_vazios[0],espacos_vazios[1]
            tabuleiro[i][j] = pc
            pontuacao_atual = minimax(tabuleiro,altura-1,False)
            tabuleiro[i][j] = vazio
            if melhor_pontuacao[2] < pontuacao_atual[2]:
                melhor_pontuacao[0] = i
                melhor_pontuacao[1] = j
                melhor_pontuacao[2] = pontuacao_atual[2]
    else:
        melhor_pontuacao = [-1,-1,10]

        for espacos_vazios in acoes(tabuleiro):
            i,j = espacos_vazios[0],espacos_vazios[1]
            tabuleiro[i][j] = humano
            pontuacao_atual = minimax(tabuleiro,altura-1,True)
            tabuleiro[i][j] = vazio
            if melhor_pontuacao[2] > pontuacao_atual[2]:
                melhor_pontuacao[0] = i
                melhor_pontuacao[1] = j
                melhor_pontuacao[2] = pontuacao_atual[2]
    
    return melhor_pontuacao

def exibe_tabuleiro(tabuleiro):
    '''
    Função que exibe o tabuleiro
    @param tabuleiro
    '''
    print(
        tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2] +
        "\n---------\n" +
        tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2] +
        "\n---------\n" +
        tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2]
    )

def jogo(tabuleiro,vez):
    '''
    Função que inicia o jogo da velha
    @param Tabuleiro,humano,pc,vez
    @return Retorna a situação final do jogo
    '''
    ## Indentifica se o jogo acabou (True) ou ainda está em andamento(False) 
    situacao_jogo = False
    vencedor = 2
    pontos = 0
    l = c = 1
    profundidade = 9 ## Profundidade máxima da árvore que será gerada

    if vez == 0:
        print("\nMáquina começa!")
    else:
        print("\nHumano começa!")

    while not(situacao_jogo):
        if vez == 0:
            print("\n> Vez de Máquina")
            l,c,pontos = minimax(tabuleiro,profundidade,True)
            resultado(tabuleiro,l,c)
            vez = 1
            profundidade -= 1
            time.sleep(2)
        else:
            print("\n> Vez de Humano")
            jogada_humano(tabuleiro)
            vez = 0
            profundidade -= 1
            time.sleep(1)
            print('- Tabuleiro')
            exibe_tabuleiro(tabuleiro)

        vencedor = ganhador(tabuleiro)
        if vencedor < 2:
            situacao_jogo = True
        elif vencedor == 2:
            situacao_jogo = True
            for i in range(3):
                for j in range(3):
                    if tabuleiro[i][j] == vazio:
                        situacao_jogo = False

    return vencedor

if __name__ == "__main__":
    print("----------Busca Competitiva----------\n")
    ## V - Vazio
    tabuleiro = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

    print("\nSorteio do 1º jogador (0 - Máquina / 1 - Humano)")
    num_sorteado = random.randrange(0,2,1)
    print("Numero sorteado: " , num_sorteado)

    resultado_jogo = jogo(tabuleiro,num_sorteado)

    if resultado_jogo == 0:
        print('Máquina venceu!')
    elif resultado_jogo == 1:
        print('Humano venceu!')
    else:
        print('Deu empate!')

    time.sleep(2)
    