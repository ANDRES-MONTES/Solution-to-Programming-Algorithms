def addBinary(a:str, b:str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
         
if __name__ == '__main__':
     a = "1010"
     b = "1011"
     result = addBinary(a, b)
     print(result)
