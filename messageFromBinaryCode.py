def solution(code:str) -> str:
    info = []
    bit = ''
    for i in range(len(code)):
        if (i + 1) % 8 == 0:
            bit += code[i]
            info.append(bit)
            bit = ''
        else:
            bit += code[i]
            
    return ''.join([chr(int(i, 2)) for i in info])
    
            




if __name__ == '__main__':
    code = "010010000110010101101100011011000110111100100001"
    result = solution(code)
    print(result)
    print(chr(int('01001000', 2)))
