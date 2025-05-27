def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    result = 0
    for i in range(1, len(timeSeries)):
        if abs(timeSeries[i - 1] - timeSeries[i]) <= duration:
            result += abs(timeSeries[i - 1] - timeSeries[i])
        else:
            result += duration
    
    result += duration
    return result
        

if __name__ == '__main__':
    timeSeries = [1,2]
    duración = 2
    result = findPoisonedDuration(timeSeries, duración)
    print(result)