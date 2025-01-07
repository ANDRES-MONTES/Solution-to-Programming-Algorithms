def solution(inputString):
    if 'a' not in inputString:
        return False
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    conteo = {}
    for i in range(len(inputString)):
        if inputString[i] not in conteo:
            conteo[inputString[i]] = 1
        else:
            conteo[inputString[i]] += 1
          
    ordenado = []
    for i in range(len(alfabeto)):
        if alfabeto[i] in conteo:
            ordenado.append((alfabeto[i], conteo[alfabeto[i]]))
        else:
            continue
    
    print(ordenado)
    
    for i in range(1, len(ordenado)):
        posicion = alfabeto.index(ordenado[i][0])
        if any(alfabeto[posicion - 1] == ordenado[i][0]  for i in range(len(ordenado))) :
            if ordenado[i][1] <= ordenado[i-1][1]:
                continue
            else:
                return False
        else:
            return False
        
        
    return True
        
if __name__ == '__main__':
    inputString = "bbbaacdafe"
    result = solution(inputString)
    print(result)