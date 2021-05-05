# -*- coding: utf-8 -*-

#cada tetrominó é uma matriz 4x4 em que 0's significam posição vazia e 1's representam o desenho da peça

#tetrominó A: AAAA

#tetrominó B: B
#             BBB

#tetrominó C:  C
#             CCC

#tetrominó D: DD
#              DD

#tetrominó E: EE
#             EE


from random import choice
import copy
#gera todos os tipos de tetrominós
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
