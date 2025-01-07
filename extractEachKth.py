def solution(inputArray, k):
    info = []
    for i in range(1, len(inputArray) + 1):
        if i % k == 0:
            info.append(i)
    
    for i in reversed(range(len(info))):
        inputArray.pop(info[i] - 1)
    
    return inputArray
        
        



if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))