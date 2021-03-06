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

    auxiliar = Tetromino(tipo)

    for i in range(27):
        auxiliar.rotaciona()
        indice = i%4 + 1
        if indice > 3:
            indice = 0
        assert rotacao[indice] == auxiliar.matriz

tipos = ('A','B','C','D','E')

@pytest.mark.parametrize("tipo",tipos)
def teste_deve_retornar_as_direcoes_certas_com_celula_cheia_a_partir_do_eixo(tipo):
    tetramino = Tetromino(tipo)

    direcoes_zero = tetramino.pega_posicoes_ocupadas()
    tetramino.rotaciona()
    direcoes_um = tetramino.pega_posicoes_ocupadas()
    tetramino.rotaciona()
    direcoes_dois = tetramino.pega_posicoes_ocupadas()
    tetramino.rotaciona()
    direcoes_tres = tetramino.pega_posicoes_ocupadas()
    tetramino.rotaciona()
    direcoes_quatro = tetramino.pega_posicoes_ocupadas()



    if tipo == 'A':
        esperado_zero = [(0,-1),(0,0),(0,1),(0,2)]
        esperado_um = [(-1,0),(0,0),(1,0),(2,0)]
        esperado_dois = [(0,-2),(0,-1),(0,0),(0,1)]
        esperado_tres = [(-2,0),(-1,0),(0,0),(1,0)]

    elif tipo == 'B':
        esperado_zero = [(-1,-1),(0,-1),(0,0),(0,1)]
        esperado_um = [(-1,0),(-1,1),(0,0),(1,0)]
        esperado_dois = [(0,-1),(0,0),(0,1),(1,1)]
        esperado_tres = [(-1,0),(0,0),(1,-1),(1,0)]

    elif tipo == 'C':
        esperado_zero = [(-1,0),(0,-1),(0,0),(0,1)]
        esperado_um = [(-1,0),(0,0),(0,1),(1,0)]
        esperado_dois = [(0,-1),(0,0),(0,1),(1,0)]
        esperado_tres = [(-1,0),(0,-1),(0,0),(1,0)]

    elif tipo =='D':
        esperado_zero = [(-1,-1),(-1,0),(0,0),(0,1)]
        esperado_um = [(-1,1),(0,0),(0,1),(1,0)]
        esperado_dois = [(0,-1),(0,0),(1,0),(1,1)]
        esperado_tres = [(-1,0),(0,-1),(0,0),(1,-1)]

    elif tipo == 'E':
        esperado_zero = [(-1,-1),(-1,0),(0,-1),(0,0)]
        esperado_um = [(-1,0),(-1,1),(0,0),(0,1)]
        esperado_dois = [(0,0),(0,1),(1,0),(1,1)]
        esperado_tres =  [(0,-1),(0,0),(1,-1),(1,0)]

    esperado_quatro = esperado_zero
    esperados = [esperado_zero,esperado_um,esperado_dois,esperado_tres,esperado_quatro]
    direcoes = [direcoes_zero,direcoes_um,direcoes_dois,direcoes_tres,direcoes_quatro]

    for i in range(5):
        assert esperados[i] == direcoes[i]
