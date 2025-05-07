def findComplement(num: int) -> int:
    return int(''.join(['1' if i == '0' else '0' for i in bin(num)[2:]]), 2)
if __name__ == '__main__':
    num = 5
    result = findComplement(num)
    print(result)