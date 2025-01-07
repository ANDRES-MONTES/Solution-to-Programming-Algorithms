def solution(inputString):
    result =''
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    print(alfabeto.index('f'))
    letras  = [x for x in alfabeto]
    for i in range(len(inputString)):
        value = letras.index(inputString[i])
        if value == len(letras) - 1:
            result += letras[0]
        else:
            result += letras[value + 1]
    
    
    
    return result


if __name__ == '__main__':
    info = 'crazy'
    result = solution(info)
    print(result)