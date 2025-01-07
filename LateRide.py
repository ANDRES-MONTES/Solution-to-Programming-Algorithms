def solution(n):
    hora = 0
    for i in range(1, n + 1):
        if i % 60 == 0:
            hora += 1
    
    minutos = n - (hora * 60)
    return  sum([int(i) for i in str(hora) + str(minutos)])
    


if __name__ == '__main__':
    n = 1439
    result = solution(n)
    print(result)