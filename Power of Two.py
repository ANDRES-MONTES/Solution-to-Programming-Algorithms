def isPowerOfTwo(n: int) -> bool:
    import math
    finder = math.log2(n)
    return 2**int(finder) == n

if __name__ == '__main__':
    n = 16
    result = isPowerOfTwo(0)
    print(result)