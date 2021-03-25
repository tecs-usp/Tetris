import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tabuleiro import Tabuleiro
from tetrominos import Tetromino
from verificador import Verificador
import copy

@pytest.fixture
def tabuleiro_vazio():
    return Tabuleiro()

def tabuleiro_com_tetramino(tabuleiro,tetramino):
    if tetramino.tipo == 'A':
        if tetramino.estado == 0:
            for j in range(tetramino.coluna - 1,tetramino.coluna + 3):
                tabuleiro.matriz[tetramino.linha][j] = 1
        elif tetramino.estado == 1:
            for i in range(tetramino.linha - 1,tetramino.linha + 3):
                tabuleiro.matriz[i][tetramino.coluna] = 1
        elif tetramino.estado == 2:
            for j in range(tetramino.coluna - 2,tetramino.coluna + 2):
                tabuleiro.matriz[tetramino.linha][j] = 1
        else:
            for i in range(tetramino.linha - 2,tetramino.linha + 2):
                tabuleiro.matriz[i][tetramino.coluna] = 1

    elif tetramino.tipo == 'B' or tetramino.tipo == 'C':

        if tetramino.estado == 0:
            for j in range(tetramino.coluna - 1, tetramino.coluna + 2):
                tabuleiro.matriz[tetramino.linha][j] = 1

            if tetramino.tipo == 'B':
                tabuleiro.matriz[tetramino.linha - 1][tetramino.coluna - 1] = 1
            else:
                tabuleiro.matriz[tetramino.linha - 1][tetramino.coluna] = 1

        if tetramino.estado == 1:
            for i in range(tetramino.linha - 1, tetramino.linha + 2):
                tabuleiro.matriz[i][tetramino.coluna] = 1

            if tetramino.tipo == 'B':
                tabuleiro.matriz[tetramino.linha - 1][tetramino.coluna + 1] = 1
            else:
                tabuleiro.matriz[tetramino.linha][tetramino.coluna + 1] = 1

        if tetramino.estado == 2:
            for j in range(tetramino.coluna - 1, tetramino.coluna + 2):
                tabuleiro.matriz[tetramino.linha][j] = 1

            if tetramino.tipo == 'B':
                tabuleiro.matriz[tetramino.linha + 1][tetramino.coluna + 1] = 1
            else:
                tabuleiro.matriz[tetramino.linha + 1][tetramino.coluna] = 1
        else:
            for i in range(tetramino.linha - 1, tetramino.linha + 2):
                tabuleiro.matriz[i][tetramino.coluna] = 1

            if tetramino.tipo == 'B':
                tabuleiro.matriz[tetramino.linha + 1][tetramino.coluna - 1] = 1
            else:
                tabuleiro.matriz[tetramino.linha][tetramino.coluna - 1] = 1

    elif tetramino.tipo == 'D':

        if tetramino.estado == 0:
            for j in range(tetramino.coluna -1, tetramino.coluna + 1):
                tabuleiro.matriz[tetramino.linha - 1][j] = 1
            for j in range(tetramino.coluna, tetramino.coluna + 2):
                tabuleiro.matriz[tetramino.linha][j] = 1

        elif tetramino.estado == 1:
            for i in range(tetramino.linha, tetramino.linha + 2):
                tabuleiro.matriz[i][tetramino.coluna] = 1
            for i in range(tetramino.linha - 1, tetramino.linha + 1):
                tabuleiro.matriz[i][tetramino.coluna + 1] = 1

        elif tetramino.estado == 2:
            for j in range(tetramino.coluna - 1, tetramino.coluna + 1):
                tabuleiro.matriz[tetramino.linha][j] = 1
            for j in range(tetramino.coluna, tetramino.coluna + 2):
                tabuleiro.matriz[tetramino.linha + 1][j] = 1
        else:
            for i in range(tetramino.linha - 1, tetramino.linha + 1):
                tabuleiro.matriz[i][tetramino.coluna] = 1
            for i in range(tetramino.linha, tetramino.linha + 2):
                tabuleiro.matriz[i][tetramino.coluna - 1] = 1

    elif tetramino.tipo == 'E':
        if tetramino.estado == 0:
            for i in range(tetramino.linha - 1, tetramino.linha + 1):
                for j in range(tetramino.coluna - 1, tetramino.coluna + 1):
                    tabuleiro.matriz[i][j] = 1
        elif tetramino.estado == 1:
            for i in range(tetramino.linha - 1, tetramino.linha + 1):
                for j in range(tetramino.coluna, tetramino.coluna + 2):
                    tabuleiro.matriz[i][j] = 1
        elif tetramino.estado == 2:
            for i in range(tetramino.linha, tetramino.linha + 2):
                for j in range(tetramino.coluna, tetramino.coluna + 2):
                    tabuleiro.matriz[i][j] = 1
        else:
            for i in range(tetramino.linha, tetramino.linha + 2):
                for j in range(tetramino.coluna - 1, tetramino.coluna + 1):
                    tabuleiro.matriz[i][j] = 1

    return tabuleiro

tipos = ['A','B','C','D','E']
@pytest.mark.parametrize("tipo",tipos)
def teste_tetraminos_devem_ser_posicionados_corretamente(tipo,tabuleiro_vazio):
    tetramino = Tetromino(tipo)

    tetramino.move("BAIXO")

    for i in range(3):
        tabuleiro_vazio_auxiliar = copy.deepcopy(tabuleiro_vazio)
        tetramino.rotaciona()
        tabuleiro_esperado = tabuleiro_com_tetramino(tabuleiro_vazio_auxiliar,tetramino)
        tabuleiro_vazio_auxiliar.coloca_tetramino(tetramino)
        assert tabuleiro_esperado == tabuleiro_vazio_auxiliar

tipos = ['A','B','C','D','E']
@pytest.mark.parametrize("tipo",tipos)
def teste_tetraminos_devem_descer_o_tabuleiro_corretamente(tipo,tabuleiro_vazio):

    tetramino = Tetromino(tipo)
    verificador = Verificador()

    for i in range(4):
        while(verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")):
            tetramino.move("BAIXO")
            tabuleiro_esperado = tabuleiro_com_tetramino(tabuleiro_vazio,tetramino)
            tabuleiro_vazio.coloca_tetramino(tetramino)
            assert tabuleiro_esperado == tabuleiro_vazio

            tabuleiro_vazio.apaga_tetramino(tetramino)

        tetramino.rotaciona()
        tetramino.linha = 0
        tetramino.coluna = 5
