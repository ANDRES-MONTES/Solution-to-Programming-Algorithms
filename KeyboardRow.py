def findWords(words: list[str]) -> list[str]:
    teclado:list[str] = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    teclado_m:list[str] = [i.upper() for i in teclado]
    output = []
    for i in range(len(words)):
        position =None
        j = 0 #ver en que posicion esta la palabra y que siempre este ahi
        current = 0
        esta = False
        while j < len(words[i]):
            if (words[i][j] not in teclado[current]) and (words[i][j] not in teclado_m[current]) :
                current += 1
                if current == 3:
                    break
            else:
                if position is None:
                    position = current
                elif position != current:
                    break
            
                
                if j == len(words[i]) - 1:
                    esta = True
                    
                j += 1
        
        if esta:
            output.append(words[i])
            esta = False
                    
    
            
    return output
    
if __name__ == '__main__':
    words = ["Hello","Alaska","Dad","Peace"]
    result = findWords(['A', 'b'])
    print(result)