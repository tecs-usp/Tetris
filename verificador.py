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
