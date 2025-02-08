def reverseBits(n: int) -> int:
    n = bin(n)[2:]
    longitud = len(n)
    if longitud == 32:
        return int(n[::-1], 2)
    else:
        n = [i for i in n]
        while len(n) < 32:
            n.insert(0,'0')
        
        return int(''.join(n[::-1]), 2)

if __name__ == '__main__':
    n = 43261596
    result  = reverseBits(n)
    print(result)
