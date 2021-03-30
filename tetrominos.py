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



#gera todos os tipos de tetrominós
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
