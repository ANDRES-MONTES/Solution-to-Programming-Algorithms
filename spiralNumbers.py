def solution(n:int) -> list:
    total = n * n
    matrix = [[ 0 for _ in range(n)] for _ in range(n)]
    shape = len(matrix)
    value = 1
        #   x, y
    iter = [0, 0]
    diagonal = 0
    while value <= total:
        for _ in range(shape):
            if _ == shape - 1:
                matrix[iter[1]][iter[0]] = value
                value += 1
            else:
                matrix[iter[1]][iter[0]] = value
                value += 1
                iter[0] += 1
            
        
        iter[1] += 1
        
        for _ in range(shape - 1):
            if _ == shape - 2:
                matrix[iter[1]][iter[0]] = value
                value += 1
                
            else:
                matrix[iter[1]][iter[0]] = value
                iter[1] += 1
                value += 1
        
        iter[0] -= 1
        
        for _ in range(shape - 1):
            if _ == shape - 2:
                matrix[iter[1]][iter[0]] = value
                value += 1
                
            else:
                matrix[iter[1]][iter[0]] = value
                iter[0] -= 1
                value += 1
        
        
        iter[1] -= 1
        for _ in range(shape - 2):
            if _ == shape - 2:
                matrix[iter[1]][iter[0]] = value
                value += 1
                
            else:
                matrix[iter[1]][iter[0]] = value
                iter[1] -= 1
                value += 1
        
        shape -= 2
        diagonal += 1
        iter = [diagonal for _ in iter]
        
    return matrix
    
            
    

if __name__ == '__main__':
    n = 3
    result = solution(n)
    for i in result:
        print(i)
    