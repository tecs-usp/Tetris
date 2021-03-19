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
            if tetramino_movido.coluna = 0 or tetramino_movido.coluna == len(tabuleiro.matriz) - 1:
                return False

        linha_inicio = tetramino_rotacionado.linha
        coluna_inicio = tetramino_rotacionado.coluna

        for linha in range( linha_inicio, len(tetramino_rotacionado.matriz) ):
            for coluna in range( coluna_inicio,  len(tetramino_rotacionado.matriz[0])):

                if tabuleiro.matriz[linha][coluna] and tetramino_rotacionado.matriz[linha][coluna]:
                    return False

        return True
