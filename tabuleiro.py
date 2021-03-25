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
