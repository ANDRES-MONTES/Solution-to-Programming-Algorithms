def toHex(num: int) -> str:
    if num == 0:
         return '0'
     
    val = ''
    simbolos = '0123456789abcdef'
    if num < 0 :
        num += 2 ** 32
    
    
    while num > 0:
        val += simbolos[num % 16]
        num = num // 16
        
                
    return val[::-1]
  
        
        
    
 
if __name__ == '__main__':
    num = -2
    result = toHex(num)
    print(result)
    print(-1%16)
