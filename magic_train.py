"""
Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este tren se mueve en un tablero representado por un array de strings.

El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del tren sigue las siguientes reglas:

Recibirás dos parámetros board y mov.

board es un array de strings que representa el tablero:

@ es la locomotora del tren.
o son los vagones del tren.
* es una fruta mágica.
· son espacios vacíos.
mov es un string que indica el próximo movimiento del tren desde la cabeza del tren @:

'L': izquierda
'R': derecha
'U': arriba
'D': abajo.
Con esta información, debes devolver una cadena de texto:

'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
'eat': Si el tren recoge una fruta mágica (*).
'none': Si avanza sin chocar ni recoger ninguna fruta mágica.
Ejemplo:

const board = [
  '·····',
  '*····',
  '@····',
  'o····',
  'o····'
]

console.log(moveTrain(board, 'U'))
// ➞ 'eat'
// Porque el tren se mueve hacia arriba y encuentra una fruta mágica

console.log(moveTrain(board, 'D'))
// ➞ 'crash'
// El tren se mueve hacia abajo y la cabeza se choca consigo mismo

console.log(moveTrain(board, 'L'))
// ➞ 'crash'
// El tren se mueve a la izquierda y se choca contra la pared

console.log(moveTrain(board, 'R'))
// ➞ 'none'
// El tren se mueve hacia derecha y hay un espacio vacío en la derecha    
"""

from typing import  Literal

def solution(board: list[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    board = [[j for j in i] for i in board]
    for i in board: print(i)
    treen = None
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '@':
                treen = (j, i)
                break
        if treen:
            break
        
    x, y = treen
    print(x, y)
    match mov:
        case 'U':
            if y - 1 < 0 or board[y - 1][x] == 'o':
                return 'crash'
            elif board[y - 1][x] == '*':
                return 'eat'
            else:
                return 'none'
    
        case 'D':
            if y + 1 > len(board) - 1 or board[y +1][x] == 'o':
                return 'crash'
            elif board[y + 1][x] == '*':
                return 'eat'
            else:
                return 'none'
            
        case 'R':
            if x + 1 > len(board[0]) - 1 or board[y][x + 1] == 'o':
                return 'crash'
            elif board[y][x + 1] == '*':
                return 'eat'
            else:
                return 'none'
        
        case 'L':
            if x - 1 < 0 or board[y][x - 1] == 'o':
                return 'crash'
            elif board[y][x - 1] == '*':
                return 'eat'
            else:
                return 'none'
        
        
        
    
    print(treen)

if __name__ == '__main__':
    board = [
        '·····',
        '*····',
        '@····',
        'o····',
        'o····'
    ]
    result = solution(board, 'L')
    print(result)