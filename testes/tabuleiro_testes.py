import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tabuleiro import Tabuleiro
from tetrominos import Tetromino
from verificador import Verificador
import copy

def tabuleiro_vazio():
    return Tabuleiro()

def tabuleiro_lotado():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

def tabuleiro_linhas_intercaladas():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1, 2):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

def tabuleiro_quase_cheio():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        if linha != 8:
            for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
                tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

tabuleiro_zerado = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] ]

tabuleiros_zeraveis = [tabuleiro_vazio(), tabuleiro_lotado(), tabuleiro_linhas_intercaladas(), tabuleiro_quase_cheio()]
@pytest.mark.parametrize("tabuleiro",tabuleiros_zeraveis)
def teste_todos_os_tabuleiros_devem_ficar_vazios(tabuleiro):
    global tabuleiro_zerado
    tabuleiro.verifica_linhas_completas()
    assert tabuleiro.matriz == tabuleiro_zerado

@pytest.fixture
def tabuleiro_celulas_intercaladas():
    tabuleiro = Tabuleiro()
    ultima_linha_de_celulas = len(tabuleiro.matriz) - 2

    for coluna in range( 1 ,len(tabuleiro.matriz[0]) - 1 ):
        tabuleiro.matriz[ultima_linha_de_celulas][coluna] = 1

    for linha in range( 0 ,ultima_linha_de_celulas ):
        if linha % 2 == 0:
            primeira_coluna = 2
        else:
            primeira_coluna = 1

        for coluna in range( primeira_coluna, len(tabuleiro.matriz[0]) - 1 , 2 ):
            tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

celulas_intercaladas = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, -1],
                        [-1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

def teste_tetrominos_devem_flutuar_sobre_celular_vazias_apos_verificacao(tabuleiro_celulas_intercaladas):
    global celulas_intercaladas

    tabuleiro_celulas_intercaladas.verifica_linhas_completas()

    assert tabuleiro_celulas_intercaladas.matriz == celulas_intercaladas

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
