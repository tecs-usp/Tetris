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
