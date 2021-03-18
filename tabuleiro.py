#o tabuleiro é uma matriz de 12X18 em que 0 representa um espaço livre, 1 representa um espaço com
#pedaços de tetrominos e -1 representa as bordas do tabuleiro


class Tabuleiro:

    def __init__(self):

        self.tabuleiro = [[0 for coluna in range(12)] for linha in range(18)]
        self.linhas_completas = []

        for linha in range(17):
            for coluna in (0,11):
                self.tabuleiro[linha][coluna] = -1

        for coluna in range(12):
            self.tabuleiro[17][coluna] = -1

    def mostra_tabuleiro(self):
        print(self.tabuleiro)

    def verifica_linhas_completas(self):
        linha = 16

        while linha > -1:
            linha_completa = True
            coluna = 1

            while linha_completa and coluna < 11:
                if self.tabuleiro[linha][coluna] == 0:
                    linha_completa = False
                coluna += 1

            if linha_completa:
                self.consome_tetrominos(linha)
                linha += 1
            linha -= 1

    def consome_tetrominos(self,linha):

        i = linha
        while (i > 0):
            for coluna in range(1,11):
                self.tabuleiro[i][coluna] = self.tabuleiro[i-1][coluna]
            i -= 1
