def solution(min1, min2_10, min11, s) -> int:
    minutes = 0
    times = 1
    while True:
        if times == 1 and s >= min1:
            s -= min1      
            minutes += 1
        elif times > 1 and times <= 10 and s >= min2_10:
            s -= min2_10
            minutes += 1
        elif times > 10 and s >= min11:
            s -= min11
            minutes += 1
        else:
            break
            
        times += 1  
    
    return minutes

if __name__ == '__main__':
    min1 = 10
    min2_10 =  1
    min11 = 2
    s =  22
    result = solution(min1, min2_10, min11, s)
    print(result)