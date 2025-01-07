def solution(n):
    if n < 10:
        return 0
    
    degree= 0
    info = list(str(n))
    
    while True:
        degree += 1
        conteo = sum([int(x) for x in info])
        if conteo < 10:
            break
        info = list(str(conteo))     
        
    return degree
        
    
    
    
if __name__ == '__main__':
    data = 57
    result = solution(data)
    print(result)