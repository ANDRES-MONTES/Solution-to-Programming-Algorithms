def sol(bishop, pawn):
    letras = 'abcdefgh'
    bishop = list(bishop)
    pawn = list(pawn)
    
    print(bishop, pawn)
    
    distancia_1, distancia_2 = letras.index(bishop[0]), letras.index(pawn[0])
    
    if abs(distancia_1 - distancia_2) == abs(int(bishop[1]) - int(pawn[1])):
        return True
    
    return False
   


if __name__ == '__main__':
    bishop =  "e7"
    pawn = "d6"
    result = sol(bishop, pawn)
    print(result)