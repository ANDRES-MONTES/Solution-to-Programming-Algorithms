def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    
    import math
    
    if 3**round(math.log(n, 3)) == n:
        return True
    
    
    return False
    
    




if __name__ == '__main__':
    
    n = 243
    result = isPowerOfThree(n)
    print(result)