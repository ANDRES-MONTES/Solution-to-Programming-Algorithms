def countBits(n: int) -> list[int]:
    return [bin(i)[2:].count('1') for i in range(n + 1)]
    


if __name__ == '__main__':
    n = 5
    result = countBits(n)
    print(result)
    print(int('1001', 2))
    print((2 & 1) +( 2 >> 1))