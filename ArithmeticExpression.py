def solution(a, b, c):
    data = ['+','-','*', '/']
    for i in range(len(data)):
        if eval(f'a{data[i]}b') == c:
            return True
    
    return False


result = solution(8, 2, 4)
print(result)
