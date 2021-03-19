# -*- coding: utf-8 -*-
#o tabuleiro é uma matriz de 12X18 em que 0 representa um espaço livre, 1 representa um espaço com
#pedaços de tetrominos e -1 representa as bordas do tabuleiro

from tetrominos import Tetromino

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
        print(self.matriz)

    def verifica_linhas_completas(self):
        linha = 16

        while linha > 0:
            linha_completa = True
            coluna = 1

            while linha_completa and coluna < 11:
                if self.matriz[linha][coluna] == 0:
                    linha_completa = False
                coluna += 1

            if linha_completa:
                self.consome_tetrominos(linha)
                linha += 1
            linha -= 1

    def consome_tetrominos(self,linha):

        i = linha
        while i > -1:
            for coluna in range(1,11):
                if i > 0:
                    self.matriz[i][coluna] = self.matriz[i-1][coluna]
                else:
                    self.matriz[i][coluna] = 0
            i -= 1

    def puxa_tetramino(self,tetramino):
        linha = tetramino.linha + 4
        coluna = tetramino.coluna

        i = linha
        while i >= tetramino.linha:
            for j in range(4):
                if i > 0 and tabuleiro.matriz[i-1][coluna] != 2 :
                    copia = tabuleiro.matriz[i-1][coluna]
                    tabuleiro.matriz[i][coluna] = copia
                else:
                    tabuleiro.matriz[i][coluna] = 0
                coluna += 1

            i -= 1

    def encaixa_tetramino(self,tetramino):
        linha = tetramino.linha
        coluna = tetramino.coluna

        for i in range(4):
            for j in range(4):
                pedaco = tetramino.matriz[i][j]
                if pedaco == 1:
                    tabuleiro.matriz[linha][coluna] = 2
                coluna += 1
            linha += 1
