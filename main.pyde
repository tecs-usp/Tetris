import time
from random import seed
from random import choice
from tabuleiro import Tabuleiro
from verificador import Verificador
from tetrominos import Tetromino


seed(1)
tipos_de_tetraminos = ['A','B','C','D','E']
tabuleiro = Tabuleiro()
tetramino = Tetromino(choice(tipos_de_tetraminos))
verificador = Verificador()
direcao = "BAIXO"
proximo_tetramino = False
inicio = time.time()
comando = False

def keyReleased():
    global comando

    comando = True

def keyPressed():
    global direcao

    if key == CODED: ###na real n precisa disso: da pra tirar o if key==CODED e deixar td junto, mas ainda vai ter que usar o keyCode em vez do key
        if keyCode == DOWN:
            direcao = "BAIXO"

        elif keyCode == UP:
            direcao = "ROTACAO"

        elif keyCode == LEFT:
            direcao = "ESQUERDA"

        elif keyCode == RIGHT:
            direcao = "DIREITA"

def principal():

    global tetramino
    global tabuleiro
    global tipos_de_tetraminos
    global verificador
    global direcao
    global proximo_tetramino
    global inicio
    global comando

    #manejo do tempo
    agora = time.time()
    diferenca_de_tempo = agora - inicio

    if diferenca_de_tempo >= 0.5:
        if verificador.cabe_tetramino(tabuleiro, tetramino,"BAIXO"):
            tabuleiro.apaga_tetramino(tetramino)
            tetramino.movimenta("BAIXO")
            tabuleiro.coloca_tetramino(tetramino)
            inicio = agora
        else:
            proximo_tetramino = True
            tabuleiro.encaixa_tetramino(tetramino)
            verificador.verifica_linhas_completas(tabuleiro)


    #lógica do jogo
    if comando:

        if verificador.cabe_tetramino(tabuleiro,tetramino,direcao):
            tabuleiro.apaga_tetramino(tetramino)

            tetramino.movimenta(direcao)
            tabuleiro.coloca_tetramino(tetramino)

        comando = False

    if proximo_tetramino:
        tetramino = Tetromino(choice(tipos_de_tetraminos))
        proximo_tetramino = False


def imprime_tabuleiro():
    global tabuleiro

    background(0)
    fill(255,182,192)
    stroke(0)

    y=height - 40

    for linha in range(0,len(tabuleiro.matriz) - 1):
        x=0
        for coluna in range(1,len(tabuleiro.matriz[0]) - 1):
            if tabuleiro.matriz[linha][coluna] != 0:
                rect(x,y,40,40)
            x += 40
        y -= 40


def setup():
    size(400, 680)
    strokeWeight(4)

def draw():
    global verificador
    global tabuleiro

    principal()

    #código para imprimir o tabuleiro após execução da lógica
    imprime_tabuleiro()

    if verificador.fim_de_jogo(tabuleiro):
        noLoop()
