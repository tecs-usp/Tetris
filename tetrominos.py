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
        self.coluna = 1

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

    def move(self,direcao):
        if direcao == "BAIXO":
            self.linha += 1
        elif direcao == "DIREITA":
            self.coluna += 1
        elif direcao =="ESQUERDA":
            self.coluna -=1


    #responsável por rotacionar os tetrominos
    def rotaciona(self,rotacao):

        #pega os angulos congruos das rotações, sendo que
        #resto == 0 -> 0º
        #resto == 1 -> 90º
        #resto == 2 -> 180º
        #resto == 3 -> 270º
        resto = rotacao%4

        if resto == 0:
            #rotacoes congruas a 0º equivalem a não rotacionar o tetromino
            return


        auxiliar = [[0 for linha in range(4)] for coluna in range(4)]

        for i in range(4):
            for j in range(4):
                auxiliar[i][j]=self.matriz[i][j]

        if resto == 1:
            coef_linha = 1
            coef_coluna = -4
            coef_linear = 12

        elif resto == 2:
            coef_linha = -4
            coef_coluna = -1
            coef_linear = 15

        elif resto == 3:
            coef_linha = -1
            coef_coluna = 4
            coef_linear = 3


        for linha in range(4):
            for coluna in range(4):
                nova_posicao = coluna*coef_coluna + coef_linha*linha + coef_linear

                if nova_posicao < 4:
                    antiga_linha = 0

                elif nova_posicao < 8:
                    antiga_linha = 1

                elif nova_posicao < 12:
                    antiga_linha = 2

                else:
                    antiga_linha = 3

                antiga_coluna = nova_posicao % 4

                self.matriz[linha][coluna] = auxiliar[antiga_linha][antiga_coluna]
