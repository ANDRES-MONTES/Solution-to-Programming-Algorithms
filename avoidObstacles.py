def sol(data:list):
    data.sort()
    i = 0
    conteo = 1
    
    while i <= data[-1]:
       if i not in data:
           i += conteo
       else:
                i = 0
                conteo += 1
    
    
    return conteo
        
        
    
        


if __name__ == '__main__':
    inputArray = [2, 3]
    result = sol(inputArray)
    print(result)