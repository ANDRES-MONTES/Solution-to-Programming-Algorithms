def sol(matriz:list):
    result = []
    rango = [[0,0], [0,1], [0,2],
             [1,0], [1,1], [1,2],
             [2,0], [2,1], [2,2]]
    copia = rango[:]
    
    ancho = len(matriz[0]) - 2
    alto = len(matriz) - 2
    
    for _ in range(alto):
        info = []
        for _ in range(ancho):
            save = []
            for i in range(len(rango)):
                save.append(matriz[rango[i][0]][rango[i][1]])
                
            value = int(sum(save) / 9)
            info.append(value)
            
            rango = [[i[0], i[1] + 1] for i in rango]
            print(rango)
        
        result.append(info[:])
        rango =  [[i[0] + 1, i[1]] for i in copia]
        copia = [[i[0] + 1, i[1]] for i in copia]
        print(rango)
    
    print(ancho)
    print(alto)
    return result



if __name__ == '__main__':
    info = [[36,0,18,9,9,45,27], 
            [27,0,54,9,0,63,90], 
            [81,63,72,45,18,27,0], 
            [0,0,9,81,27,18,45], 
            [45,45,27,27,90,81,72], 
            [45,18,9,0,9,18,45], 
            [27,81,36,63,63,72,81]]
    
    reuslt = sol(info)
    for i in reuslt:
        print(i)