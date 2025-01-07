def solution(a, b, c):
    data = {}
    info = [a, b, c]
    for i in range(len(info)):
        if info[i] not in data:
            data[info[i]] = 1
        else:
            data[info[i]] += 1
    

    return list(filter(lambda x : x[1] == 1, data.items()))[0][0]
    
 


if __name__ == '__main__':
    a = 2
    b = 7
    c = 2
    result = solution(a, b, c)
    print(result)