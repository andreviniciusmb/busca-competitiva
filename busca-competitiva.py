import random
import time

humano = 'O' ## Marcador do jogador huamno
pc = 'X'     ## Marcador do jogador PC
vazio = '-'  ## Marcador do estado vazio

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
            aux = False
    
    print('Linha: ' + str(linha) + ' - Coluna: ' + str(coluna))

def continua(tabuleiro):
    '''
    Retorna se o jogo continua (True) ou não (False).
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
    Retorna Verdadeiro o ganhador do jogo
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

def maxValor(a,b):
    '''
    Retorna o maior valor entre dois numeros.
    @param Dois números inteiros
    @return Um número inteiro
    '''
    if a > b:
        return a
    else:
        return b

def minValor(a,b):
    '''
    Retorna o menor valor entre dois numeros.
    @param Dois números inteiros
    @return Um número inteiro
    '''
    if a < b:
        return a
    else:
        return b

def minimax(tabuleiro,profundidade,ehMaximo):
    '''
    Retorna a jogada ótima para o jogador atual baseado no algoritmo de minimax
    @param Tabuleiro,profundidade da árvore, se a pontuação é máxima ou não
    @return Pontuação da jogada.
    '''
    pontos = custo(tabuleiro)
    if pontos == 1:
        return pontos
    elif pontos == -1:
        return pontos
    
    if not(continua(tabuleiro)):
        return 0
    
    if ehMaximo:
        melhor_pontuacao = -100000

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == vazio:
                    tabuleiro[i][j] = pc
                    melhor_pontuacao = maxValor(melhor_pontuacao,minimax(tabuleiro,profundidade+1,not(ehMaximo)))
                    tabuleiro[i][j] = vazio
        return melhor_pontuacao
    else:
        melhor_pontuacao = 100000

        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == vazio:
                    tabuleiro[i][j] = humano
                    melhor_pontuacao = minValor(melhor_pontuacao,minimax(tabuleiro,profundidade+1,not(ehMaximo)))
                    tabuleiro[i][j] = vazio
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

def acoes(tabuleiro):
    '''
    Procura a melhor ação e retorna a posição do melhor movimento.
    @param Tabuleiro
    @return Lista com dois números inteiros
    '''
    melhor_pontuacao = -10
    pontuacao_atual = -10
    melhor_movimento = [1,1]

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                tabuleiro[i][j] = pc
                pontuacao_atual = maxValor(melhor_pontuacao,minimax(tabuleiro,0,False))
                tabuleiro[i][j] = vazio
                if pontuacao_atual > melhor_pontuacao:
                    melhor_pontuacao = pontuacao_atual
                    melhor_movimento = [i,j]
    return melhor_movimento

def jogo(tabuleiro,vez):
    '''
    Função que inicia o jogo da velha
    @param Tabuleiro,humano,pc,vez
    @return Retorna a situação final do jogo
    '''
    ## Indentifica se o jogo acabou (True) ou ainda está em andamento(False) 
    situacao_jogo = False
    vencedor = 2
    l = c = 1
    if vez == 0:
        print("\nMáquina começa!")
    else:
        print("\nHumano começa!")

    while not(situacao_jogo):
        if vez == 0:
            print("\n> Vez de Máquina")
            l,c = acoes(tabuleiro)
            resultado(tabuleiro,l,c)
            vez = 1
            time.sleep(2)
        else:
            print("\n> Vez de Humano")
            jogada_humano(tabuleiro)
            vez = 0
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
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
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
    