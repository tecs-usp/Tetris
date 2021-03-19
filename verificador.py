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
        elif direcao == "DIREITA" or direcao == "ESQUERDA":
            tetramino_movido.move(direcao)
            if tetramino_movido.coluna = 0 or tetramino_movido.coluna == len(tabuleiro.matriz) - 1:
                return False
        else:
            tetramino_movido.move(direcao)
            if tetramino_movido.linha == len(tabuleiro.matriz) - 4:
                return False

        linha_inicio = tetramino_movido.linha
        coluna_inicio = tetramino_movido.coluna
        i=0
        j=0

        for linha in range( linha_inicio, len(tetramino_movido.matriz) ):
            for coluna in range( coluna_inicio,  len(tetramino_movido.matriz[0])):

                if (tabuleiro.matriz[linha][coluna] == 2) and tetramino_movido.matriz[i][j]:
                    return False
                j += 1

            i += 1

        return True
