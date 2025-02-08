def titleToNumber(columnTitle: str) -> int:
    column = 0
    for i in range(len(columnTitle)):
        value = (ord(columnTitle[i]) - ord('A')) + 1
        column = column * 26 + value
    
    return column

def titleToNumber_2(columnTitle: str) -> int:
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    conteo =0
    for i in range(len(columnTitle)):
        position = values.index(columnTitle[i]) + 1
        conteo = conteo * 26 + position
    
    return conteo


if __name__ == '__main__':
    val = 'LLX'
    result = titleToNumber(val)
    pther = titleToNumber_2(val)
    print(result)    
    print(pther)     
     
