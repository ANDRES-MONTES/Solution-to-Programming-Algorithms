def islandPerimeter(grid: list[list[int]]) -> int:
    perimetro = 0
    ancho = len(grid[0]) - 1
    alto = len(grid) - 1
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total = 4
            if grid[i][j] == 1:
                if (i - 1 >= 0) and (grid[i - 1][j] == 1):
                    total -= 1
                if (i + 1 <= alto) and (grid[i + 1][j] == 1):
                    total -= 1 
                if (j - 1 >= 0) and (grid[i][j - 1] == 1):
                    total -= 1 
                if (j + 1 <= ancho) and (grid[i][j + 1] == 1):
                    total -= 1 
                
                perimetro += total
    
    return perimetro
            
                

    
if __name__ == '__main__':
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    result = islandPerimeter(grid)
    print(result)
