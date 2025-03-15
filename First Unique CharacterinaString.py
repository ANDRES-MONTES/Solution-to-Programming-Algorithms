def firstUniqChar(s: str) -> int:
    from collections import Counter
    data = Counter(s)
    for i in data:
        if data[i] == 1:
            return s.index(i)
        
    return -1


    
        
    



if __name__ == '__main__':
    var = 'aabb'
    result = firstUniqChar(var)
    print(result)
