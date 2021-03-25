import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tetrominos import Tetromino
from tabuleiro import Tabuleiro
from verificador import Verificador

@pytest.fixture
def tabuleiro_vazio():
    return Tabuleiro()

tetrominos = ['A','B','C','D','E']

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_devem_movimentarse_livremente_ao_surgir_em_tabuleiro_vazio(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ROTACAO")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_atravessar_parede_esquerda_do_tabuleiro(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)

    tetramino.move("BAIXO")
    limite_para_a_esquerda = tetramino.coluna - 2

    for i in range(limite_para_a_esquerda):
        assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")
        tetramino.move("ESQUERDA")

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_atravessar_parede_direita_do_tabuleiro(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)

    tetramino.move("BAIXO")

    if tipo == 'A':
        limite_para_direita = tetramino.coluna - 2

    elif tipo == 'B' or tipo == 'C' or tipo == 'D':
        limite_para_direita = tetramino.coluna - 1

    elif tipo == 'E':
        limite_para_direita = tetramino.coluna

    for i in range(limite_para_direita):
        assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")
        tetramino.move("DIREITA")

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_nao_devem_atravessar_o_chao_do_tabuleiro(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    for descida in range(len(tabuleiro_vazio.matriz) - 1):
        tetramino.move("BAIXO")

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")




def coloca_parede_interna(tabuleiro):

    coluna = 5
    for linha in range(len(tabuleiro.matriz) - 1 ):
        tabuleiro.matriz[linha][coluna] = 2

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_ultrapassar_paredes_verticais_de_encaixes(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")

    tetramino.move("DIREITA")
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")
    coloca_parede_interna(tabuleiro_vazio)

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_ultrapassar_celula_unica_de_encaixes(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)

    tabuleiro_vazio.matriz[tetramino.linha + 1][tetramino.coluna] = 2
    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")

def tabuleiro_lotado():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 2

    return tabuleiro

def tabuleiro_linhas_intercaladas():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1, 2):
        for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
            tabuleiro.matriz[linha][coluna] = 2

    return tabuleiro

def tabuleiro_quase_cheio():
    tabuleiro = Tabuleiro()

    for linha in range( 1, len(tabuleiro.matriz) - 1 ):
        if linha != 8:
            for coluna in range( 1 , len(tabuleiro.matriz[0]) - 1 ):
                tabuleiro.matriz[linha][coluna] = 2

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

tabuleiros_zeraveis = [Tabuleiro(), tabuleiro_lotado(), tabuleiro_linhas_intercaladas(), tabuleiro_quase_cheio()]
@pytest.mark.parametrize("tabuleiro",tabuleiros_zeraveis)
def teste_todos_os_tabuleiros_devem_ficar_vazios(tabuleiro):
    global tabuleiro_zerado
    verificador = Verificador()
    verificador.verifica_linhas_completas(tabuleiro)
    assert tabuleiro.matriz == tabuleiro_zerado

@pytest.fixture
def tabuleiro_celulas_intercaladas():
    tabuleiro = Tabuleiro()
    ultima_linha_de_celulas = len(tabuleiro.matriz) - 2

    for coluna in range( 1 ,len(tabuleiro.matriz[0]) - 1 ):
        tabuleiro.matriz[ultima_linha_de_celulas][coluna] = 2

    for linha in range( 0 ,ultima_linha_de_celulas ):
        if linha % 2 == 0:
            primeira_coluna = 2
        else:
            primeira_coluna = 1

        for coluna in range( primeira_coluna, len(tabuleiro.matriz[0]) - 1 , 2 ):
            tabuleiro.matriz[linha][coluna] = 2

    return tabuleiro

celulas_intercaladas = [[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, -1],
                        [-1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1],
                        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

def teste_tetrominos_devem_flutuar_sobre_celular_vazias_apos_verificacao(tabuleiro_celulas_intercaladas):
    global celulas_intercaladas

    verificador  = Verificador()

    verificador.verifica_linhas_completas(tabuleiro_celulas_intercaladas)

    assert tabuleiro_celulas_intercaladas.matriz == celulas_intercaladas
