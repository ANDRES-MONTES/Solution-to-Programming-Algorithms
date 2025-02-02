def convertToTitle(columnNumber: int) -> str:
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    columna = ''
    
    if (columnNumber - 1) // 26 < 1:
        val = columnNumber % 26
        columna += alfabeto[val - 1]
        return columna
    
    else:
        val = (columnNumber) % 26
        other = convertToTitle((columnNumber - 1)//26)
        columna += alfabeto[val - 1]
        print(other)
        return other + columna 
    
    
if __name__ == '__main__':
    columnNumber = 52
    result = convertToTitle(columnNumber)
    print(result)
    print(51%26)
