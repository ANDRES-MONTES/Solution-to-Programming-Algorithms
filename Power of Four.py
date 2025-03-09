def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    
    import math
    if 4 ** round(math.log(n, 4)) == n:
        return True
    
    return False 

    
if __name__ == '__main__':
    n = 32
    result = isPowerOfFour(n)
    print(result)