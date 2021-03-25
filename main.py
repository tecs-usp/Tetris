from tabuleiro import Tabuleiro
from tetrominos import Tetromino
from verificador import Verificador

fim_de_jogo = False
tabuleiro = Tabuleiro()
verificador = Verificador()

while not fim_de_jogo:

    #código para lidar com o tempo


    #código para pegar os inputs do usuário


    #lógica do jogo
    tabuleiro.apaga_tetramino(tetramino)
    if verificador.cabe_tetramino(tabuleiro,tetramino,direcao):

        tetramino.movimenta(direcao)

        if not verificador.cabe_tetramino(tabuleiro,tetramino,"BAIXO"):
            proximo_tetramino = 1
            tabuleiro.encaixa_tetramino(tetramino)
            verificador.verifica_linhas_completas(tabuleiro)
        else:
            tabuleiro.coloca_tetramino(tetramino)

    if verificador.fim_de_jogo(tabuleiro):
        fim_de_jogo = True

    elif not proximo_tetramino:
            tetramino.movimenta("BAIXO")

    else:
        tetramino = Tetramino(#aleatorizar tipo de tetramino)
        proximo_tetramino = 0

     #código para imprimir o tabuleiro após execução da lógica
