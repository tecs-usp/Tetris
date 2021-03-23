# -*- coding: utf-8 -*-
import copy
from tetrominos import Tetromino

#Classe responsável por verificar se as movimentações do tetraminó inputadas pelo jogador são possíveis
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

        for linha in range(linhas):
            for coluna in range(colunas):
                if tetramino_movido.matriz[linha][coluna]:

                    if linha_inicio + linha >= len(tabuleiro.matriz) - 1:
                        return False
                    if coluna_inicio + coluna >= len(tabuleiro.matriz[0]) - 1:
                        return False
                    if coluna_inicio + coluna < 1:
                        return False

        linha_final =  linha_inicio + len(tetramino_movido.matriz)
        coluna_final = coluna_inicio + len(tetramino_movido.matriz[0])
        i=0        
        for linha in range( linha_inicio, linha_final ):
            j=0
            for coluna in range( coluna_inicio, coluna_final ):

                if (tabuleiro.matriz[linha][coluna] == 2) and tetramino_movido.matriz[i][j]:
                    return False
                j += 1

            i += 1

        return True
