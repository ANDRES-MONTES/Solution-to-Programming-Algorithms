def convertToBase7(num: int) -> str:
    if num == 0: return '0'
    
    negativo = False
    if num < 0: 
        negativo = True
        num = -1 * num
    base = ''
    while num > 0:
        val = num % 7
        base += str(val)
        num = num // 7
        
    if negativo:
        return '-' + base[::-1]
        
    return base[::-1]

if __name__ == '__main__':
    num = 100
    result = convertToBase7(-7)
    print(result)