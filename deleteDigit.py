def solution(n:int) -> int:
    info = [x for x in str(n)]
    data = []
    for i in range(len(info)):
        pivot = info[:]
        pivot.pop(i)
        data.append(pivot[:])
    
    print(data)
    
    data = [int(''.join(i)) for i in data]
    return max(data)
    
    
    
    
if __name__ == '__main__':
    n = 152
    result = solution(n)
    print(result)