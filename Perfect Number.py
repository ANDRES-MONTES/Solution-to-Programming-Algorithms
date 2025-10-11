def checkPerfectNumber(num: int) -> bool:
    colect = num
    from collections import Counter    
    divisors:list[int] = []
    i = 2
    while i * i <= num:
        while num % i == 0:
            divisors.append(i)
            num //= i
        i += 1
        
    if num > 1:
         divisors.append(num)
        
    print(divisors)
    conteo = Counter(divisors)
    potencias = [(i, [j for j in range(0, conteo[i] + 1)]) for i in conteo]
    re_potencias = []
    print(potencias)
    for i in range(len(potencias)):
        data = []
        for j in range(len(potencias[i][1])):
            data.append(potencias[i][0] ** potencias[i][1][j])
        re_potencias.append(data[:])

            
    print(re_potencias)
    output = []
    #Multiplica todos los valores con todos y cada uno de los siguientes 
    for i in range(len(re_potencias) - 1):
        j = 0
        while j < len(re_potencias[i]):
            for k in range(len(re_potencias[i + 1])):
                output.append(re_potencias[i][j] * re_potencias[i + 1][k])
            j += 1
    
    vals = list(set(output))
    try:
        vals.remove(colect)
    except:
        pass
    if sum(vals) == colect:
        return True
    
    return False


if __name__ == '__main__':
    num = 28
    result = checkPerfectNumber(7)
    print(result)