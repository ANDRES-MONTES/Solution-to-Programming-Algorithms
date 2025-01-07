def solution(time:str) -> bool:
    time = time.split(':')
    time = [int(i) for i in time]
    if time[0] >= 0 and time[0] < 24 and time[1] >= 0 and time[1] < 60:
        return True
    
    return False
    
    print(time)



if __name__ == '__main__':
    time =  "25:51"
    result = solution(time)
    print(result)
    