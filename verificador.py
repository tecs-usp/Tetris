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

        for linha in range(len(tetramino_movido.matriz)):
            for coluna in range(len(tetramino_movido.matriz[0])):
                if tetramino_movido.matriz[linha][coluna]:

                    if linha_inicio + linha >= len(tabuleiro.matriz) - 1:
                        return False
                    if coluna_inicio + coluna >= len(tabuleiro.matriz[0]) - 1:
                        return False

        i=0
        for linha in range( linha_inicio, len(tetramino_movido.matriz) - 1):
            j=0
            for coluna in range( coluna_inicio,  len(tetramino_movido.matriz[0]) - 1):

                if (tabuleiro.matriz[linha][coluna] == 2) and tetramino_movido.matriz[i][j]:
                    return False
                j += 1

            i += 1

        return True
