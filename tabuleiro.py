# -*- coding: utf-8 -*-
#o tabuleiro é uma matriz de 12X18 em que 0 representa um espaço livre, 1 representa um espaço com
#pedaços de tetrominos e -1 representa as bordas do tabuleiro

from tetrominos import Tetromino

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
