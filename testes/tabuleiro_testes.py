import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tabuleiro import Tabuleiro

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
