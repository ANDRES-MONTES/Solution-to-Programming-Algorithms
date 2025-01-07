def solution(matrix:list) -> int:
    info = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            positions = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
            data = [matrix[x[0]][x[1]] for x in positions]
            info.append(data)
           
            
    print(info)
    info = set([tuple(i) for i in info])
    return len(info)
                
    

if __name__ == '__main__':
    matrix=[[1, 2, 1],
            [2, 2, 2],
            [2, 2, 2],
            [1, 2, 3],
            [2, 2, 1]]
    result = solution(matrix)
    print(result)
