import time, copy
from random import seed
from random import choice
from tabuleiro import Tabuleiro
from tetrominos import Tetromino
from verificador import Verificador

tipos_de_tetraminos = ['A','B','C','D','E']
tabuleiro = Tabuleiro()
tetramino = Tetromino(choice(tipos_de_tetraminos))
verificador = Verificador()
direcao = "BAIXO"
proximo_tetramino = False
inicio = time.time()
tecla_valida = False

def keyPressed():
    global direcao, tecla_valida

    if key == CODED:
        if keyCode == DOWN:
            direcao = "BAIXO"
            tecla_valida = True

        elif keyCode == UP:
            direcao = "ROTACAO"
            tecla_valida = True

        elif keyCode == LEFT:
            direcao = "ESQUERDA"
            tecla_valida = True

        elif keyCode == RIGHT:
            direcao = "DIREITA"
            tecla_valida = True
        else:
            tecla_valida = False
    else:
        tecla_valida = False

def principal():

    global tetramino, tabuleiro, tipos_de_tetraminos, verificador, direcao, proximo_tetramino, inicio, tecla_valida

    #manejo do tempo
    agora = time.time()
    diferenca_de_tempo = agora - inicio

    if diferenca_de_tempo >= 0.5:
        if verificador.cabe_tetramino(tabuleiro, tetramino,"BAIXO"):
            tabuleiro.apaga_tetramino(tetramino)
            tetramino.movimenta("BAIXO")
            tabuleiro.coloca_tetramino(tetramino,1)
            inicio = agora
        else:
            proximo_tetramino = True
            tabuleiro.coloca_tetramino(tetramino,2)
            verificador.verifica_linhas_completas(tabuleiro)


    #logica do jogo
    if tecla_valida and diferenca_de_tempo>=0.2:

        if verificador.cabe_tetramino(tabuleiro,tetramino,direcao):
            tabuleiro.apaga_tetramino(tetramino)

            tetramino.movimenta(direcao)
            tabuleiro.coloca_tetramino(tetramino,1)

        tecla_valida = False

    if proximo_tetramino:
        tetramino = Tetromino(choice(tipos_de_tetraminos))
        proximo_tetramino = False


def imprime_tabuleiro():
    global tabuleiro, cores, tetramino

    background(255,255,255)
    stroke(255,255,255)

    y=0
    for linha in range(0,len(tabuleiro.matriz) - 1):
        x=0
        for coluna in range(1,len(tabuleiro.matriz[0]) - 1):
            if tabuleiro.matriz[linha][coluna] != 0:
                fill(*tabuleiro.matriz_de_cores[linha][coluna])
                rect(x,y,40,40)
            x += 40
        y += 40


def setup():
    size(400, 680)
    strokeWeight(4)
    noCursor()

def draw():
    global verificador, tabuleiro
    
    principal() # funcionalidades principais

    imprime_tabuleiro() # imprimir tabuleiro após execução da lógica

    # condição de fim de jogo
    if verificador.fim_de_jogo(tabuleiro):
        noLoop()
