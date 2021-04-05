import time
from random import seed
from random import choice
from tabuleiro import Tabuleiro
from verificador import Verificador
from tetrominos import Tetromino
from animador import Animador

tipos_de_tetraminos = ['A','B','C','D','E']
tabuleiro = Tabuleiro()
tetramino = Tetromino(choice(tipos_de_tetraminos))
verificador = Verificador()
animador = Animador()
direcao = "BAIXO"
proximo_tetramino = False
inicio = time.time()
tecla_valida = False
linhas_completas = []
animacao_de_linha_completa = False

def keyPressed():
    global direcao
    global tecla_valida

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

    global tetramino
    global tabuleiro
    global tipos_de_tetraminos
    global verificador
    global animador
    global direcao
    global proximo_tetramino
    global inicio
    global tecla_valida
    global linhas_completas
    global animacao_de_linha_completa

    #manejo do tempo
    agora = time.time()
    diferenca_de_tempo = agora - inicio

    if diferenca_de_tempo >= 0.5:

        if len(linhas_completas) > 0:
            for linha in linhas_completas:
                tabuleiro.limpa_linha(linha)

            linhas_completas=[]

        if verificador.cabe_tetramino(tabuleiro, tetramino,"BAIXO"):
            tabuleiro.apaga_tetramino(tetramino)
            tetramino.movimenta("BAIXO")
            tabuleiro.coloca_tetramino(tetramino)
            inicio = agora
        else:
            proximo_tetramino = True
            tabuleiro.encaixa_tetramino(tetramino)
            linhas_completas = verificador.verifica_linhas_completas(tabuleiro)
            if len(linhas_completas) > 0:
                animador.pinta_linhas_completas(tabuleiro,linhas_completas)
                animacao_de_linha_completa = True



    #lógica do jogo
    if tecla_valida and diferenca_de_tempo>=0.2 and not proximo_tetramino:

        if verificador.cabe_tetramino(tabuleiro,tetramino,direcao):
            tabuleiro.apaga_tetramino(tetramino)

            tetramino.movimenta(direcao)
            tabuleiro.coloca_tetramino(tetramino)

        tecla_valida = False

    if proximo_tetramino:
        tetramino = Tetromino(choice(tipos_de_tetraminos))
        proximo_tetramino = False


def imprime_tabuleiro():
    global tabuleiro
    global cores
    global tetramino

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
    global verificador
    global tabuleiro
    global animacao_de_linha_completa
    global inicio

    principal()

    if animacao_de_linha_completa:
        delay(3000)
        inicio = time.time()
        animacao_de_linha_completa = False


    #código para imprimir o tabuleiro após execução da lógica
    imprime_tabuleiro()

    if verificador.fim_de_jogo(tabuleiro):
        noLoop()
