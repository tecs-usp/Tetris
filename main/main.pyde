import time, copy
from random import seed
from random import choice

class Tabuleiro:

    def __init__(self):

        self.matriz = [[0 for coluna in range(12)] for linha in range(18)]
        self.linhas_completas = []
        self.matriz_de_cores = [[[255,255,255] for coluna in range(len(self.matriz[0]))] for linha in range(len(self.matriz))]

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
                        self.matriz_de_cores[i][coluna]=self.matriz_de_cores[i-1][coluna]
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
                self.matriz_de_cores[linha + movimento[0]][coluna + movimento[1]] = [255,255,255]

    def coloca_tetramino(self,tetramino,encaixe):

        #define as instrucoes para colocar os tijolos no tabuleiro
        #a partir de suas posicoes em relacao ao referencial eixo de rotacao.
        #Ja que o eixo de rotacao eh o primeiro tijolo a ser colocado
        #no tabuleiro apos movimentacao, a posicao de todos os outros
        #pode ser definida por sua posicao relativa eo eixo referencial
        caminho = tetramino.pega_posicoes_ocupadas()

        #guarda a posicao a partir de qual os blocos de tijolos serao encaixados
        #Ex: coloque um tijolo uma linha acima e duas colunas a direita da atual
        referencial_linha = tetramino.linha
        referencial_coluna = tetramino.coluna

        for direcao in caminho:
            referencial_linha = tetramino.linha
            referencial_coluna = tetramino.coluna
            referencial_linha += direcao[0]
            referencial_coluna +=  direcao[1]
            if referencial_linha > -1:
                self.matriz[referencial_linha][referencial_coluna] = encaixe
                self.matriz_de_cores[referencial_linha][referencial_coluna] = tetramino.cor


class Tetromino:

    #cria os tetrominos como matrizes a depender de seu tipo (A,B,C,D ou E)
    def __init__(self,tipo):

        self.matriz = [[0 for coluna in range(4)] for linha in range(4)]

        #Marcam a referencial principal para localizar um  tetramino na matriz do tabuleiro,
        #que eh seu eixo de rotacao
        #No init, essa posicao eh no centro da primeira linha. Sao modificados
        #pelo metodo move()
        self.linha = 0
        self.coluna = 5

        #atributo que diz qual das 4 posicoes possiveis para cada tetramino
        #é a atual. Essas posições são definidas para os valores [0,1,2,3],
        #a cada input UP o valor é incrementado pelo método rotaciona()
        #voltando para o estado inicial após a 3a rotação.
        self.estado = 0

        self.tipo = tipo

        #marcam a posicao em relacao a matriz do tabuleiro que o eixo do tetramino se encontra
        #no init, essa posicao eh no centro da primeira linha. Sao modificados
        #pelo metodo
        self.eixo_linha = 3
        self.eixo_coluna = 1

        self.cor = choice([(247, 168, 184),(242, 201, 212),(160, 219, 242),(85, 205, 252)])

        if tipo == 'A':
            self.matriz = [[0,0,0,0],
                           [0,0,0,0],
                           [0,0,0,0],
                           [1,1,1,1]]

        elif tipo == 'B':
            self.matriz = [[0,0,0,0],
                           [0,0,0,0],
                           [1,0,0,0],
                           [1,1,1,0]]

        elif tipo == 'C':
            self.matriz = [[0,0,0,0],
                           [0,0,0,0],
                           [0,1,0,0],
                           [1,1,1,0]]

        elif tipo == 'D':
            self.matriz = [[0,0,0,0],
                           [0,0,0,0],
                           [1,1,0,0],
                           [0,1,1,0]]

        elif tipo == 'E':
            self.matriz = [[0,0,0,0],
                           [0,0,0,0],
                           [1,1,0,0],
                           [1,1,0,0]]

    def movimenta(self,direcao):
        if direcao != "ROTACAO":
            self.move(direcao)
        else:
            self.rotaciona()

    #translada o tetramino pelo tabuleiro
    def move(self,direcao):
        if direcao == "BAIXO":
            self.linha += 1
        elif direcao == "DIREITA":
            self.coluna += 1
        elif direcao =="ESQUERDA":
            self.coluna -=1


    #rotaciona o tetramino
    def rotaciona(self):

        self.estado += 1
        #limita o estado do tetramino para apenas para valores menores
        #que quatro
        self.estado = self.estado % 4

        auxiliar = copy.deepcopy(self.matriz)

        for linha in range(4):
            for coluna in range(4):
                #a relação entre a posicao dos tijolos do tetramino antes e apos uma rotacao
                #pode ser descrita por um sistema linear de variaveis que relacionam a antiga
                #e a nova posicao de cada tijolo

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

                #apos rotacao, a posicao do eixo de rotacao do tetramino deve ser atualizada
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

    #retorna quais sao as posicoes ocupadas pelos tijolos
    #na matriz do tetramino. Essas posicoes sao definidas
    #pelo caminho que deve ser feito a partir do tijolo
    #do eixo de rotacao para se chegar nos outros tijolos
    def pega_posicoes_ocupadas(self):

        caminho = []

        linha = self.eixo_linha
        coluna = self.eixo_coluna

        i = 0
        while(i < len(self.matriz)):
            j = 0
            while( j < len(self.matriz[0])):
                if self.matriz[i][j]:
                    #os caminhos para o tijolo do eixo tem direcao e sentido. a direcao eh
                    #horizontal ou vertical. O sentido eh avancando ou retrocedendo
                    #nos indices de linha ou coluna
                    distancia_linha = i - linha
                    distancia_coluna = j - coluna

                    caminho.append((distancia_linha, distancia_coluna))
                j += 1
            i += 1

        return caminho

class Verificador:

    def __init__(self):
        pass

    def cabe_tetramino(self,tabuleiro,tetramino,direcao):

        #e o teramino que sera movimentado de acordo com a direcao
        #input para verificar se hah ou nao colisao
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
            #verifica se a nova posicao de algum tijolo apos movimentacao
            #do tetramino colidira com posicao jah ocupada no tabuleiro
            linha_ocupada = linha_inicio + movimento[0]
            coluna_ocupada = coluna_inicio + movimento[1]

            #impede que o tetramino atravesse as paredes do tabuleiro
            if linha_ocupada >= len(tabuleiro.matriz) - 1:
                return False
            if coluna_ocupada >= len(tabuleiro.matriz[0]) - 1:
                return False
            if coluna_ocupada <= 0:
                return False

            #impede que o tetramino se movimente para posicao jah ocupada
            if linha_ocupada > -1:
                if tabuleiro.matriz[linha_ocupada][coluna_ocupada] == 2:
                    return False

        return True


    #procura por alguma linha completa de tijolos pelo tabuleiro
    def verifica_linhas_completas(self,tabuleiro):
        linha = len(tabuleiro.matriz) - 2

        while linha > 0:
            linha_completa = True
            coluna = 1

            while linha_completa and coluna < (len(tabuleiro.matriz[0]) - 1):
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


tipos_de_tetraminos = ['A','B','C','D','E']
tabuleiro = Tabuleiro()
tetramino = Tetromino(choice(tipos_de_tetraminos))
verificador = Verificador()
direcao = "BAIXO"
proximo_tetramino = False
inicio = time.time()
tecla_valida = False

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
    global direcao
    global proximo_tetramino
    global inicio
    global tecla_valida

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

    principal()

    #código para imprimir o tabuleiro após execução da lógica
    imprime_tabuleiro()

    if verificador.fim_de_jogo(tabuleiro):
        noLoop()
