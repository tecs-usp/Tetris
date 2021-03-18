import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

from tetrominos import Tetromino


tetromino_a = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [1,1,1,1]]

tetromino_b = [[0,0,0,0],
               [0,0,0,0],
               [1,0,0,0],
               [1,1,1,0]]

tetromino_c = [[0,0,0,0],
               [0,0,0,0],
               [0,1,0,0],
               [1,1,1,0]]

tetromino_d = [[0,0,0,0],
               [0,0,0,0],
               [1,1,0,0],
               [0,1,1,0]]

tetromino_e = [[0,0,0,0],
               [0,0,0,0],
               [1,1,0,0],
               [1,1,0,0]]


verificar = [('A',tetromino_a),('B',tetromino_b),('C',tetromino_c),('D',tetromino_d),('E',tetromino_e)]

@pytest.mark.parametrize("matriz_esperada",verificar)
def testa_se_os_tetrominos_sao_montados_certo(matriz_esperada):
    instancia_da_matriz = Tetromino(matriz_esperada[0])
    assert matriz_esperada[1] == instancia_da_matriz.matriz

rotacoes_a = [[[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [1,1,1,1]],

              [[1,0,0,0],
               [1,0,0,0],
               [1,0,0,0],
               [1,0,0,0]],

              [[1,1,1,1],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]],

              [[0,0,0,1],
               [0,0,0,1],
               [0,0,0,1],
               [0,0,0,1]]]

rotacoes_b = [[[0,0,0,0],
               [0,0,0,0],
               [1,0,0,0],
               [1,1,1,0]],

              [[1,1,0,0],
               [1,0,0,0],
               [1,0,0,0],
               [0,0,0,0]],

              [[0,1,1,1],
               [0,0,0,1],
               [0,0,0,0],
               [0,0,0,0]],

              [[0,0,0,0],
               [0,0,0,1],
               [0,0,0,1],
               [0,0,1,1]]]

rotacoes_c = [[[0,0,0,0],
              [0,0,0,0],
              [0,1,0,0],
              [1,1,1,0]],

             [[1,0,0,0],
              [1,1,0,0],
              [1,0,0,0],
              [0,0,0,0]],

             [[0,1,1,1],
              [0,0,1,0],
              [0,0,0,0],
              [0,0,0,0]],

             [[0,0,0,0],
              [0,0,0,1],
              [0,0,1,1],
              [0,0,0,1]]]

rotacoes_d = [[[0,0,0,0],
              [0,0,0,0],
              [1,1,0,0],
              [0,1,1,0]],

             [[0,1,0,0],
              [1,1,0,0],
              [1,0,0,0],
              [0,0,0,0]],

             [[0,1,1,0],
              [0,0,1,1],
              [0,0,0,0],
              [0,0,0,0]],

             [[0,0,0,0],
              [0,0,0,1],
              [0,0,1,1],
              [0,0,1,0]]]

rotacoes_e = [[[0,0,0,0],
               [0,0,0,0],
               [1,1,0,0],
               [1,1,0,0]],

              [[1,1,0,0],
               [1,1,0,0],
               [0,0,0,0],
               [0,0,0,0]],

              [[0,0,1,1],
               [0,0,1,1],
               [0,0,0,0],
               [0,0,0,0]],

              [[0,0,0,0],
               [0,0,0,0],
               [0,0,1,1],
               [0,0,1,1]]]

rotacoes = [('A',rotacoes_a),('B',rotacoes_b),('C',rotacoes_c),
            ('D',rotacoes_d),('E',rotacoes_e)]

@pytest.mark.parametrize("tipo,rotacao",rotacoes)
def testa_rotacoes(tipo, rotacao):
    auxiliar = [[0 for linha in range(4)]for coluna in range(4)]

    for i in range(27):
        auxiliar = Tetromino(tipo)
        auxiliar.rotaciona(i)
        assert rotacao[i%4] == auxiliar.matriz
