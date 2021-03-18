import os, sys, pytest

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
diretorio_pai = os.path.dirname(diretorio_atual)
sys.path.append(diretorio_pai)

import tetrominos


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

@pytest.mark.parametrize("matriz",verificar)
def testa_se_os_tetrominos_sao_montados_certo(matriz):
    assert matriz[1] == tetrominos.tetromino(matriz[0])

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

rotacoes = [(tetromino_a,rotacoes_a),(tetromino_b,rotacoes_b),(tetromino_c,rotacoes_c),
            (tetromino_d,rotacoes_d),(tetromino_e,rotacoes_e)]

@pytest.mark.parametrize("matriz_base,rotacao",rotacoes)
def testa_rotacoes(matriz_base, rotacao):
    auxiliar = [[0 for linha in range(4)]for coluna in range(4)]

    for i in range(27):
        for linha in range(4):
            for coluna in range(4):
                auxiliar[linha][coluna] = matriz_base[linha][coluna]

        assert rotacao[i%4] == tetrominos.rotaciona(auxiliar,i)
