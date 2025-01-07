def plusOne(digits:list[int]) -> list[int]:
    data:list = [str(i) for i in digits]
    return  [int(i) for i in str(int(''.join(data)) + 1)]
    

if __name__ == '__main__':
    digits = [9]
    result = plusOne(digits)
    print(result)