def isBadVersion(version: int) -> bool:
    if version >= 1:
        return True
    return False


def firstBadVersion(n: int) -> int:    
    if n == 1:
        return 1

    value = [1, n]
    while abs(value[0] - value[1]) != 1:
        amount = round(sum(value) / 2)
        check = isBadVersion(amount)
        if check:
            value[1] = amount
        else:
            value[0] = amount
    
    if isBadVersion(value[0]):
        return value[0]
    else:
        return value[1]
    
if __name__ == '__main__':
    bad = 4
    result = firstBadVersion(1)
    print(result)
    