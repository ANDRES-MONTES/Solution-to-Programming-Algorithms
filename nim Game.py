def canWinNim(n: int) -> bool:
    if n % 4 == 0:
        return False
    
    return True

if __name__ == '__main__':
    n = 4
    result  = canWinNim(n)
    print(result)