import copy
from tetrominos import Tetromino

#Classe responsável por verificar se as movimentações do tetraminó inputadas pelo jogador são possíveis
class Verificador:

    def __init__(self):
        pass

    def tetramino_pode_rotacionar(self,tabuleiro,tetramino,rotacao):
        tetramino_rotacionado = copy.deepcopy(tetramino)
        tetramino_rotacionado.rotaciona(rotacao)

        linha_inicio = tetramino_rotacionado.linha
        coluna_inicio = tetramino_rotacionado.coluna

        for linha in range( linha_inicio, len(tetramino_rotacionado.matriz) ):
            for coluna in range( coluna_inicio,  len(tetramino_rotacionado.matriz[0])):

                if tabuleiro.matriz[linha][coluna] and tetramino_rotacionado.matriz[linha][coluna]:
                    return False

        return True

    def cabe_tetramino(self,tabuleiro,tetramino,movimento):

        tetramino_movido = copy.deepcopy(tetramino)
        tetramino_movido.empurra(movimento)

        for linha in range( tetramino_movido.linha, len(tetramino_movido.matriz) ):
            for coluna in range( tetramino_movido.coluna, len(tetramino_movido.matriz[0]) ):
                if tabuleiro.matriz[linha][coluna] and tetramino_movido.matriz[linha][coluna]:
                    return False

        return True
