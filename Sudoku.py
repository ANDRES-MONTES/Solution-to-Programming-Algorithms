def solution(grid:list) -> bool:
    row = grid[:]
    row = [set(row[i]) for i in range(len(row))]
    for i in range(len(row)):
        if len(row[i]) == 9:
            continue
        else:
            return False
        
    column = grid[:]    
    column = [set([j[i] for j in column]) for i in range(len(column[0]))]
    for i in range(len(column)):
        if len(column[i]) == 9:
            continue
        else:
            return False
    
    
    ventana = [[0,0],[0,1],[0,2],
               [1,0],[1,1],[1,2],
               [2,0],[2,1],[2,2],]
    
    backup = ventana[:]    
    cuadricula = []
    j = 0
    for _ in range(9):
        j += 1
        data = []
        for i in range(len(ventana)):
            data.append(grid[ventana[i][0]][ventana[i][1]])
        cuadricula.append(data)
        
        ventana = [[i[0], i[1] + 3] for i in ventana]
        
        if j == 3:
            ventana = [[ventana[i][0] + 3, backup[i][1]] for i in range(len(ventana))]
            j = 0
            

    cuadricula = [set(i) for i in cuadricula]
    for i in range(len(cuadricula)):
        if len(cuadricula[i]) == 9:
            continue
        else:
            return False
    
    return True
            
    
if __name__ == '__main__':
    grid = [[1,3,2,5,4,6,9,8,7],
            [4,6,5,8,7,9,3,2,1],
            [7,9,8,2,1,3,6,5,4],
            [9,2,1,4,3,5,8,7,6],
            [3,5,4,7,6,8,2,1,9],
            [6,8,7,1,9,2,5,4,3],
            [5,4,6,9,8,1,4,3,2],
            [2,7,3,6,5,7,1,9,8],
            [8,1,9,3,2,4,7,6,5]]
    result = solution(grid)
    print(result)
