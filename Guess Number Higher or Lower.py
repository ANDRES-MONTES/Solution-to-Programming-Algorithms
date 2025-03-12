#
def guess(num: int) -> int:
    if num > 12:
        return -1
    if num < 12:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    rango = [1, n]
    
    while True:
        option =round( (rango[0] + rango[1]) / 2)
        val = guess(option)
        if val == -1:
            rango[1] = option - 1
            
        elif val == 1:
            rango[0] = option + 1
        else:
            return option
        
        if rango[1] - rango[0] == 1:
            val = guess(rango[0])
            if val == 0:
                return rango[0]
            else:
                return rango[1]
                
        

if __name__ == '__main__':
    n =100
    result = guessNumber(n)
    print(result)
    