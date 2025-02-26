def isUgly(n: int) -> bool:
    if n <= 0:
            return False
        
    primos = [2, 3, 5]
    i = 0
    while n > 1:
        if n % primos[i] == 0:
            n /= primos[i]
        else:
            i += 1
            if i > len(primos) -1:
                return False
            
    return True
        
        


if __name__ == '__main__':
    n = 6
    result = isUgly(10)
    print(result)
