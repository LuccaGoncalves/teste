tabuleiro = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
turnos = 0
print('Levando em consideração as posições abaixo :')
print('\n L0 C0 | L0 C1 | L0 C2 ')
print(f'{"_"*7}|{"_"*7}|{"_"*7}\n L1 C0 | L1 C1 | L1 C2 ')
print(f'{"_"*7}|{"_"*7}|{"_"*7}\n L2 C0 | L2 C1 | L2 C2 \n{" "*7}|{" "*7}|{" "*7}\n')

def expTabuleiro():
    for linha in tabuleiro:
        print(f'     |     |     ')
        print(f'  {linha[0]}  |  {linha[1]}  |  {linha[2]}  ')
        print(f'_____|_____|_____')
    print()

def verificarWin(jogador):
    linhas = tabuleiro
    colunas = [[tabuleiro[i][j] for i in range(3)] for j in range(3)]
    diagonais = [[tabuleiro[i][i] for i in range(3)], [tabuleiro[i][2-i] for i in range(3)]]
    todas = linhas + colunas + diagonais
    return [jogador] * 3 in todas

while turnos < 9:
    jogador = 'X' if turnos % 2 == 0 else 'O'
    linha = int(input(f'Jogador {jogador}, selecione a linha que deseja jogar: '))
    coluna = int(input(f'Jogador {jogador}, selecione a coluna que deseja jogar: '))
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('Posição inválida. Tente novamente.')
        continue
    if tabuleiro[linha][coluna] != '_':
        print('Posição inválida. Tente novamente.')
        continue
    tabuleiro[linha][coluna] = jogador
    expTabuleiro()
    if verificarWin(jogador):
        print(f'Jogador {jogador} é o vencedor!')
        break
    turnos += 1
if turnos == 9:
    print('Deu velha!')
