def isPerfectSquare(num: int) -> bool:
    if num < 0:
        return False
    if num == 1:
        return True
    
    val = num // 2
    for _ in range(20):
        x = (val/2) + (num/(2*val))
        print(x)
        if round(x) ** 2 == num:
            return True
        val = x
        
    return False
    
    
if __name__ == '__main__':
    num = 808201
    result = isPerfectSquare(num)
    print(result)
    import math
    print(math.sqrt(808201))
    
    
    