def findRelativeRanks(score: list[int]) -> list[str]:
    medallas = score.copy()
    medallas.sort(reverse=True)
    ranking = medallas[:3]
    puestos = ["Gold Medal","Silver Medal","Bronze Medal"]
    data = {medallas[i]:puestos[i] for i in range(len(ranking))}
    for i in range(len(score)):
        if i > len(ranking) - 1:
            data[medallas[i]] = str(i + 1)
        
    output = []
    for i in range(len(score)):
        output.append(data[score[i]])
        
    return output
    

if __name__ == '__main__':
    score = [10,3,8,9,4]
    result = findRelativeRanks(score)
    print(result)