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
def teste_tetraminos_nao_devem_atravessar_a_parede_esquerda_do_tabuleiro(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_devem_conseguir_se_mover_para_a_direita_em_tabuleiros_vazios(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_devem_conseguir_se_mover_para_baixo_em_tabuleiros_vazios(tipo ,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_devem_conseguir_rotacionar_em_tabuleiros_vazios(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ROTACAO")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetraminos_nao_devem_atravessar_o_chao_do_tabuleiro(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)
    for descida in range(14):
        tetramino.move("BAIXO")

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")




def coloca_parede_interna(tabuleiro):

    coluna = 1
    for linha in range(len(tabuleiro.matriz) - 1 ):
        tabuleiro.matriz[linha][coluna] = 2

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_ultrapassar_paredes_verticais_de_encaixes(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)

    assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"DIREITA")

    tetramino.move("DIREITA")
    coloca_parede_interna(tabuleiro_vazio)
    print(tetramino.coluna)

    assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"ESQUERDA")

@pytest.mark.parametrize("tipo",tetrominos)
def teste_tetrominos_nao_devem_ultrapassar_celula_unica_de_encaixes(tipo,tabuleiro_vazio):
    verificador = Verificador()
    tetramino = Tetromino(tipo)

    tabuleiro_vazio.matriz[4][1] = 2

    if tipo != 'D':
        assert not verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")
    else:
        assert verificador.cabe_tetramino(tabuleiro_vazio,tetramino,"BAIXO")
