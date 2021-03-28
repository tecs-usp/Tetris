import time, copy
from random import seed
from random import choice

class Tabuleiro:

    def __init__(self):

        self.matriz = [[0 for coluna in range(12)] for linha in range(18)]
        self.linhas_completas = []

        for linha in range(17):
            for coluna in (0,11):
                self.matriz[linha][coluna] = -1

        for coluna in range(12):
            self.matriz[17][coluna] = -1

    def mostra_matriz(self):
        for linha in range(18):
            print(self.matriz[linha])

    def limpa_linha(self,linha):

        i = linha
        while i > -1:
            for coluna in range(1,len(self.matriz[0]) - 1):
                if self.matriz[i][coluna] != 1 and  self.matriz[i-1][coluna] != 1:
                    if i > 0:
                        self.matriz[i][coluna] = self.matriz[i-1][coluna]
                    else:
                        self.matriz[i][coluna] = 0
            i -= 1

    def apaga_tetramino(self,tetramino):
        linha = tetramino.linha
        coluna = tetramino.coluna

        caminho_tetramino = tetramino.pega_posicoes_ocupadas()

        for movimento in caminho_tetramino:
            i = linha + movimento[0]
            if i>=0:
                self.matriz[linha + movimento[0]][coluna + movimento[1]] = 0

    def coloca_tetramino(self,tetramino):
        posicoes = tetramino.pega_posicoes_ocupadas()

        linha = tetramino.linha
        coluna = tetramino.coluna

        for posicao in posicoes:
            linha = tetramino.linha
            coluna = tetramino.coluna
            linha += posicao[0]
            coluna +=  posicao[1]
            self.matriz[linha][coluna] = 1



    def encaixa_tetramino(self,tetramino):
        posicoes = tetramino.pega_posicoes_ocupadas()

        linha = tetramino.linha
        coluna = tetramino.coluna

        for posicao in posicoes:
            linha = tetramino.linha
            coluna = tetramino.coluna
            linha += posicao[0]
            coluna +=  posicao[1]
            self.matriz[linha][coluna] = 2


class Tetromino:

    #cria os tetrominos como matrizes a depender de seu tipo (A,B,C,D ou E)
    def __init__(self,tipo):

        self.matriz = [[0 for coluna in range(4)] for linha in range(4)]
        self.linha = 0
        self.coluna = 5
        self.estado = 0
        self.tipo = tipo
        self.eixo_linha = 3
        self.eixo_coluna = 1

        if tipo == 'A':
            i=3
            j=0
            while(j<4):
                self.matriz[i][j]=1
                j+=1

        elif tipo == 'B':
            i=2
            j=0

            self.matriz[i][j]=1
            i+=1

            while(j<3):
                self.matriz[i][j]=1
                j+=1

        elif tipo == 'C':
            i=2
            j=1

            self.matriz[i][j]=1
            i+=1
            j=0

            while(j<3):
                self.matriz[i][j]=1
                j+=1

        elif tipo == 'D':
            i=2
            j=0

            self.matriz[i][j]=1
            j+=1
            self.matriz[i][j]=1
            i+=1

            while(j<3):
                self.matriz[i][j]=1
                j+=1

        elif tipo == 'E':
                i=2
                j=0

                while(i<4):
                    while(j<2):
                        self.matriz[i][j]=1
                        j+=1

                    i+=1
                    j=0

    def movimenta(self,direcao):
        if direcao != "ROTACAO":
            self.move(direcao)
        else:
            self.rotaciona()

    def move(self,direcao):
        if direcao == "BAIXO":
            self.linha += 1
        elif direcao == "DIREITA":
            self.coluna += 1
        elif direcao =="ESQUERDA":
            self.coluna -=1


    #responsável por rotacionar os tetrominos
    def rotaciona(self):

        self.estado += 1
        self.estado = self.estado % 4
        auxiliar = [[0 for linha in range(4)] for coluna in range(4)]

        for i in range(4):
            for j in range(4):
                auxiliar[i][j]=self.matriz[i][j]

        for linha in range(4):
            for coluna in range(4):
                nova_posicao = -4*coluna + linha + 12

                if nova_posicao < 4:
                    nova_linha = 0

                elif nova_posicao < 8:
                    nova_linha = 1

                elif nova_posicao < 12:
                    nova_linha = 2

                else:
                    nova_linha = 3

                nova_coluna = nova_posicao % 4

                self.matriz[linha][coluna] = auxiliar[nova_linha][nova_coluna]

                self.muda_posicao_eixo()

    def muda_posicao_eixo(self):

        if self.estado == 0:
            self.eixo_linha = 3
            self.eixo_coluna = 1

        elif self.estado == 1:
            self.eixo_linha = 1
            self.eixo_coluna = 0

        elif self.estado == 2:
            self.eixo_linha = 0
            self.eixo_coluna =2

        else:
            self.eixo_linha = 2
            self.eixo_coluna = 3

    def pega_posicoes_ocupadas(self):

        posicoes = []

        linha = self.eixo_linha
        coluna = self.eixo_coluna

        i = 0
        while(i < len(self.matriz)):
            j = 0
            while( j < len(self.matriz[0])):
                if self.matriz[i][j]:
                    distancia_linha = i - linha
                    distancia_coluna = j - coluna
                    posicoes.append((distancia_linha, distancia_coluna))
                j += 1
            i += 1

        return posicoes

class Verificador:

    def __init__(self):
        pass

    def cabe_tetramino(self,tabuleiro,tetramino,direcao):

        tetramino_movido = copy.deepcopy(tetramino)
        if direcao == "ROTACAO":
            tetramino_movido.rotaciona()
        else:
            tetramino_movido.move(direcao)

        linha_inicio = tetramino_movido.linha
        coluna_inicio = tetramino_movido.coluna
        linhas = len(tetramino_movido.matriz)
        colunas =  len(tetramino_movido.matriz[0])
        caminho_tetramino = tetramino_movido.pega_posicoes_ocupadas()

        for movimento in caminho_tetramino:
            linha_ocupada = linha_inicio + movimento[0]
            coluna_ocupada = coluna_inicio + movimento[1]

            if linha_ocupada >= len(tabuleiro.matriz) - 1:
                return False
            if coluna_ocupada >= len(tabuleiro.matriz[0]) - 1:
                return False
            if coluna_ocupada <= 0:
                return False

        for movimento in caminho_tetramino:
            linha_ocupada = linha_inicio + movimento[0]
            coluna_ocupada = coluna_inicio + movimento[1]
            if linha_ocupada > -1:
                if tabuleiro.matriz[linha_ocupada][coluna_ocupada] == 2:
                    return False

        return True

    def verifica_linhas_completas(self,tabuleiro):
        linha = len(tabuleiro.matriz) - 2

        while linha > 0:
            linha_completa = True
            coluna = 1

            while linha_completa and coluna < 11:
                if tabuleiro.matriz[linha][coluna] != 2:
                    linha_completa = False
                coluna += 1

            if linha_completa:
                tabuleiro.limpa_linha(linha)
                linha += 1
            linha -= 1

    def fim_de_jogo(self,tabuleiro):
        for coluna in range(1,len(tabuleiro.matriz[0]) - 1):
            if tabuleiro.matriz[0][coluna] == 2:
                return True

        return False
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

    if key == CODED:
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

    y=0

    for linha in range(0,len(tabuleiro.matriz) - 1):
        x=0
        for coluna in range(1,len(tabuleiro.matriz[0]) - 1):
            if tabuleiro.matriz[linha][coluna] != 0:
                rect(x,y,40,40)
            x += 40
        y += 40


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
