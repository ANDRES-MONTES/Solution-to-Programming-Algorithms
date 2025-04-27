def countLargestGroup(n: int) -> int:
    data = {}
    maximo = 0
    for i in range(1, n + 1):
        value = str(i)
        total = sum(int(i) for i in value)
        
        if total not in data:
            data[total] = [i]
        else:
            data[total].append(i)
            
        maximo = max(maximo, len(data[total]))
            
    return sum(1 for grupo in data.values() if len(grupo) == maximo)
            
        
        


if __name__ == '__main__':
    n = 46
    result = countLargestGroup(n)
    print(result)
