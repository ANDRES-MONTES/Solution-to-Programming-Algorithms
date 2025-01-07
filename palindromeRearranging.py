def sol(arr:str):
    info = [x for x in arr]
    data = {}
    
    
    if len(info) % 2 == 0:
        for i in range(len(info)):
            if info[i] not in data:
                data[info[i]] = 1
            else:
                data[info[i]] +=  1
        
        for i in data.values():
            if i % 2 != 0:
                return False
        
        return True
                
    elif len(info) % 2 != 0:
        for i in range(len(info)):
            if info[i] not in data:
                data[info[i]] = 1
            else:
                data[info[i]] += 1
        print(data)
        solo_una = 0
        for i in data.values():
            if i == 1:
                solo_una += 1
        
        print(solo_una)
        if solo_una > 1:
            return False
        
        return True

    
if __name__ == '__main__':
    examples = 'zzzzzzzll' # ddbbccaa dbcaacbd dbcacdb  p  p
    result = sol(examples)
    print(result)
    