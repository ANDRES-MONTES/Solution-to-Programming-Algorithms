"""
Estás atrapado en una pesadilla en la que Freddy Krueger te persigue 😭. El sueño está representado por un laberinto de celdas, donde cada celda tiene un valor numérico que indica el nivel de peligro de esa parte del sueño.

Debes encontrar el camino más seguro (es decir, el que tenga el menor valor total de peligro) desde la esquina superior izquierda hasta la esquina inferior derecha de la matriz.

En este desafío, solo puedes moverte hacia la derecha o hacia abajo (no puedes retroceder ni moverte en diagonal) y debes calcular el nivel total de peligro del camino más seguro.

La pesadilla está representada por una matriz dream de tamaño n x m donde cada celda es un número positivo que representa el nivel de peligro de esa celda en el sueño.

Y tienes que devolver el valor total de peligro del camino más seguro de la esquina superior izquierda (posición [0][0]) a la esquina inferior derecha (posición [n-1][m-1]).

const dream = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
]    
"""

def sol(matriz:list[int]) -> int:
    [[1, 2, 3, 4],
     [1, 2, 3, 4]
     [1, 2, 3, 4]
     [1, 2, 3, 4]]

if __name__ == '__main__':
    ream = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1], ]    
    result = sol(ream)
    print(result)