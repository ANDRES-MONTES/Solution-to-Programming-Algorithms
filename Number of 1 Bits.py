def hammingWeight(n: int) -> int:
    n = bin(n)[2:]
    return n.count('1')
    

if __name__ == '__main__':
    n = 2147483645
    result  = hammingWeight(n)
    print(result)
