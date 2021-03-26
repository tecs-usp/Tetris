# Tetris com Processin

Implementação do famoso (e viciante) jogo inventado na União Soviética na década de 80.
...
### Lógica
Toda a lógica para o jogo foi escrita em Python (versão 3.8.5).
...
### As classes do jogo
O jogo é baseado em apenas três classe:

- Tabuleiro : Representante de todos as posições ocupadas ou potencialmente ocupadas pelos tetraminós.
               Possui métodos para limpar suas linhas, encaixar tetraminós permanente ou temporariamente (quando ainda estão em quedas)

- Tetromino : Representante das peças do Tetris. Possui métodos para se transladar e rotacionar, além de
               um método que retorna exatamente a localização das partes dessas peças na matriz que as representa.

- Verificador: Representante da entidade responsável por verificar aspectos sensíveis à funcionalidade  do jogo. Possui método para verificar se determinado tetraminó cabe  em  determinada posição do tabuleiro baseado em sua posição atual e no movimento que se deseja fazer (de acordo com a entrada do jogador). Possui método para verificar se alguma linha do tabuleiro está completa (o que configura pontuação ao jogador) e se é ou não game over.
...
### Gráficos e loop do jogo
A interface gráfica do jogo e a maneira de implementação de seu loop principal são baseadas no [Processing](https://processing.org/overview/ "Processing Overview")(versão 3.5.4). Utiliou-se, evidentemente, o [Processing modo Python](https://py.processing.org/ "Python Mode for Processing")
...
### Dependências
Para que o jogo possa ser executado:
..*[Processing](https://processing.org/download/ "Download")

Para que os testes possam ser executados (localizados no diretório testes/):
..*[Pytest](https://docs.pytest.org/en/stable/getting-started.html "Installation Guide)
...
### Como executar o jogo:
Estando com o Processing em modo Python devidamente instalado e aberto em seu computador, abrir o código main/main.pyde . Após aberto, é só clicar no botão de executar do Processing :).
...
### Por que e para quem este jogo foi desenvolvido
Sendo Tetris um jogo com muita popularidade e relativa simplicidade de implementação, ele foi escolhido para ser o software final a ser desenvolvido pelos alunos do curso de introdução à lógica de programação oferecido pelo Grupo de Trabalho LGBTecs - parte do [Tecs](https://tecs.ime.usp.br/).

Além de sustentada na popularidade do jogo, a escolha por ele baseou-se em seu elevado potencial de edição gráfica (cores  e formas dos tetraminós, animações de pontuações e game over, etc), algo considerado importante pelo grupo que o desenvolveu, uma vez que o jogo será o principal fator de atração dos futuros estudantes ao curso.
...
### Por que Processing Modo Python?
...
Escolheu-se Processing em modo Python para ser a linguagem de programação do jogo devido a alguns fatores principais:
⋅⋅* Processing é um software livre. Ou seja, se encaixa perfeitamente nos princípios que guiam o grupo autor deste projeto
..* Python é uma das linguagens de programação mais populares atualmente. Sendo um dos objetivos do curso que utilizará este projeto a motivação dos alunos em ingressar de fato em carreiras na computação, introduzi-los a este mundo por meio de uma linguagem com alta procura no mercado atual foi prioridade.
..* Python possui uma sintaxe extremamente simples e é, portanto, fácil de ser aprendida por aqueles que nunca tiveram contato com programação.
.Agradecimento especial ao autor do [vídeo]..
### Agradecimentos
Agradecimento especial a todos os membros do LGBTecs e do Tecs que contribuíram no desenvolvimento deste jogo.
