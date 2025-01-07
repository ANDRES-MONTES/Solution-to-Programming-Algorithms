def solution(cell):
    movimientos = [(1, -2), (2, -1), (2, 1), (1, 2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    
    letter = 'abcdefgh'
    caballo = letter.index(cell[0]) + 1
    posicion = (int(cell[1]), caballo)
    print(posicion)
    muertes = 0
    
    for i in range(len(movimientos)):
        y = posicion[0] + movimientos[i][0]
        x = posicion[1] + movimientos[i][1]
        
        if y > 0 and y <= 8 and x > 0 and x <= 8:
            muertes += 1
    
    return muertes
        
    


if __name__ == '__main__':
    cell = 'g6'
    result = solution(cell)
    print(result) 