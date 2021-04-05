class Animador:

    def __init__(self):
        pass

    def pinta_linhas_completas(self,tabuleiro,linhas_completas):

        comprimento_linha = len(tabuleiro.matriz_de_cores[0]) - 2

        tamanho_azul = comprimento_linha//3

        tamanho_branco = comprimento_linha - 2*tamanho_azul


        for linha in linhas_completas:
            for coluna in range(1,len(tabuleiro.matriz_de_cores[linha]) - 1):
                if coluna < tamanho_azul:
                    tabuleiro.matriz_de_cores[linha][coluna] = [85, 205, 252] #azul

                elif coluna < tamanho_azul + tamanho_branco:
                    tabuleiro.matriz_de_cores[linha][coluna] =  [255, 255, 255] #branco

                else:
                    tabuleiro.matriz_de_cores[linha][coluna] = [247, 168, 184] #rosa
