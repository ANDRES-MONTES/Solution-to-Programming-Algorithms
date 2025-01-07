def sol(matrix:list):
    campo = [[0 for _ in i] for i in matrix]    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > 0:
                if matrix[i - 1][j] == True:
                    campo[i][j] += 1
            
            if i < len(matrix) - 1:
                if matrix[i + 1][j] == True:
                    campo[i][j] += 1
            
            if j > 0:
                if matrix[i][j - 1] == True:
                    campo[i][j] += 1
            
            if j < len(matrix[i]) - 1:
                if matrix[i][j + 1] == True:
                    campo[i][j] += 1
                    
            if i > 0 and j > 0:
                if matrix[i - 1][j -1] == True:
                     campo[i][j] += 1
            
            if i < len(matrix) - 1 and j > 0:
                if matrix[i + 1][j - 1] == True:
                    campo[i][j] += 1
                    
            if i > 0 and j < len(matrix[i]) - 1:
                if matrix[i - 1][j + 1] == True:
                    campo[i][j]+= 1
                    
            if i < len(matrix) - 1 and j < len(matrix[i]) - 1:
                if matrix[i + 1][j + 1] == True:
                    campo[i][j]+= 1
            
    return campo
                        
    
if __name__ == '__main__':
    info =  [[True, False, False],
             [False, True, False],
             [False, False, False],]
    
    result = sol(info)
    for i in result:
        print(i)