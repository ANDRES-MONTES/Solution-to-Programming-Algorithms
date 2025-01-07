"""
Estamos programando unos robots llamados giftbot 🤖🎁 que navegan de forma autónoma por los almacenes de regalos.

Estamos creando una función a la que le pasamos: el almacén 🏬 que deben navegar y los movimientos ↔️ que pueden realizar.

El almacén se representa como un array de cadenas de texto, donde:

. significa que hay vía libre.
* significa que hay un obstáculo.
! es la posición inicial del robot.
Los movimientos son un array de cadenas de texto, donde:

R mueve al robot una posición a la derecha.
L mueve al robot una posición a la izquierda.
U mueve al robot una posición hacia arriba.
D mueve al robot una posición hacia abajo.
Hay que tener en cuenta que el robot no puede superar los obstáculos ni los límites del almacén.

Dados un almacén y los movimientos, debemos devolver el array con la posición final de nuestro robot.

const store = ['..!....', '...*.*.']

const movements = ['R', 'R', 'D', 'L']
const result = autonomousDrive(store, movements)
console.log(result)
/*
[
  ".......",
  "...*!*."
]
*/

// El último movimiento es hacia la izquierda, pero no puede moverse porque hay un obstáculo.
Ten en cuenta que la store es un array que puede ser de un número de filas que va de 1 a 100, ya que tenemos almacenes de todos los tamaños.

También que el robot es posible que termine en su posición inicial si no puede moverse o si está dando vueltas. 
    
"""
import time

def autonomus_driver(store:list, movements:list):
    matriz = [list(store[i]) for i in range(len(store))]
    x = None
    y = None
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == '!':
                x = j
                y = i
     
    for i in range(len(movements)):
        if movements[i] == 'R':
            if x == len(matriz[y]) - 1:
                continue
            if matriz[y][x + 1] == '.':
                matriz[y][x], matriz[y][x + 1] = '.', '!'
                x += 1
                
        if movements[i] == 'L':
            if x == 0:
                continue
            if matriz[y][x - 1] == '.':
                matriz[y][x - 1], matriz[y][x] = '!', '.'
                x-= 1
                
        if movements[i] == 'U':
            if y == 0:
                continue
            if matriz[y - 1][x] == '.':
                matriz[y - 1][x], matriz[y][x] = '!', '.'
                y -= 1
        
        
        if movements[i] == 'D':
            if y == len(matriz) - 1:
                continue
            if matriz[y + 1][x] == '.':
                 matriz[y][x], matriz[y + 1][x] = '.', '!'
                 y += 1
            
          
          
          
    result = [''.join(matriz[i]) for i in range(len(matriz))]
    return result




if __name__ == '__main__':
    tienda = [
        '..!....', 
        '...*.*.'
        ]
    
    mio = [
        '....!................',
        '.....................',
        '***...........*******',
        '*******........******',
        '**********....*******',
        '***********...*******',
        '****..........*******',
    ]
    movimientos =  ['R', 'R', 'D', 'L']
    mi_movimientos = ['D', 'D', 'R', 'R', 'R', 'R','R','D']
    result = autonomus_driver(mio, mi_movimientos)






