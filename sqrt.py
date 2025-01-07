def mySqrt(x:int) -> int:
    val:int = 0
    while val * val < x:
        val += 1
        if val * val > x:
            return val -1
    return val

if __name__ == '__main__':
    data = 8
    result = mySqrt(data)
    print(result)
