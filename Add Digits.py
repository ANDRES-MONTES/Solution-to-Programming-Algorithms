def addDigits(num: int) -> int:
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9



if __name__ == '__main__':
    num = 38
    result = addDigits(69)
    print(result)
    print(1000%9)
    print(1%9)

