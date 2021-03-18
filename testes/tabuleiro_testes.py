import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tabuleiro import Tabuleiro

@pytest.fixture
def tabuleiro_vazio():
    return Tabuleiro()

@pytest.fixture
def tabuleiro_lotado():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

@pytest.fixture
def tabuleiro_intercalado():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1, 2):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro

@pytest.fixture
def tabuleiro_quase_cheio():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        if linha != 8:
            for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
                tabuleiro.matriz[linha][coluna] = 1

    return tabuleiro


tabuleiro_zerado = [ [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
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

def teste_todos_os_tabuleiros_devem_ficar_vazios(tabuleiro_vazio,tabuleiro_lotado,tabuleiro_intercalado,tabuleiro_quase_cheio):
    print(tabuleiro_vazio)
    global tabuleiro_zerado

    tabuleiro_vazio.verifica_linhas_completas()
    tabuleiro_lotado.verifica_linhas_completas()
    tabuleiro_intercalado.verifica_linhas_completas()
    tabuleiro_quase_cheio.verifica_linhas_completas()

    assert tabuleiro_vazio.matriz == tabuleiro_zerado
    assert tabuleiro_lotado.matriz == tabuleiro_zerado
    assert tabuleiro_intercalado.matriz == tabuleiro_zerado
    assert tabuleiro_quase_cheio.matriz == tabuleiro_zerado
