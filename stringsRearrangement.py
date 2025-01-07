def sol(n:list):
    import itertools
    info  = [[x for x in i] for i in n]
    convinaciones = list(itertools.permutations(info))  
    for i in convinaciones:
        print(i)
    
    for i in range(len(convinaciones)):
        for j in range(len(convinaciones[i]) - 1):
            errores = 0
            for x in range(len(convinaciones[i][j])):
                if errores == 2:
                    break
                if convinaciones[i][j][x] not in convinaciones[i][j + 1][x]:
                    errores += 1
                else: 
                    continue
            if errores == 2:
                break
            elif errores == 0:
                break
        if errores > 0 and errores < 2:
            return True
            
            
    return False
                
            
        
    
            
         
        
            
    
    
        
    


if __name__ == '__main__':
    data = ["aba", "bbb", "bab"]
    data_2 = ["ab", "bb", "aa",]
    data_3 = ["q", "q"]
    data_4 = ["abc", "abx", "axx", "abc"]
    result = sol(data_4)
    print(result)