def solution(product:int) -> int:    
    if product == 0:
        return 10
    if product == 1:
        return 1
    
    n = 9
    divisor = []
    while product > 1:
        if product % n == 0:
            divisor.append(n)
            product = product / n
            if n == 1:
                break
        else:
            n -= 1
    print(divisor)
    if 1 in divisor:
        return -1
               
    return int(''.join([str(i) for i in divisor][::-1])) 
       
        


if __name__ == '__main__':
    product = 450#- 2559
    result = solution(product)
    print(result)