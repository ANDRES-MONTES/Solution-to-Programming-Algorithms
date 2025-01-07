def sol(cell1, cell2):
    tablero = [[0 for i in range(8)] for i in range(8)]
    negro = True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if negro:
                tablero[i][j] = 0
                negro = False
            else:
                tablero[i][j] = 1
                negro = True
                
    tablero = [tablero[i] if i % 2 == 0 else tablero[i][::-1] for i in range(8)]
    letras = 'abcdefgh'
    posiciones = {letras[i] : tablero[i] for i in range(len(letras))}
    print(posiciones)
        
    info = [list(cell1), list(cell2)]
    info = [[i[0].lower(), int(i[1])] for i in info]
    if posiciones[info[0][0]][info[0][1] - 1] == posiciones[info[1][0]][info[1][1] - 1]:
        return True
    return False
        

    
    
                
            


if __name__ == '__main__':
    cell1 = 'A1'
    cell2 = 'H3'
    result = sol(cell1, cell2)
    print(result)