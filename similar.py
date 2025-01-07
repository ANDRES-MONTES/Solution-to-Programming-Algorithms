def sol(a:list, b:list):
    if a == b:
        return True
    if len(a) != len(b):
        return False
    
    diferences = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diferences.append((i, a[i], b[i]))
            
        if len(diferences) > 2:
            return False
    
    if len(diferences) != 2:
        return False
    else:
        a[diferences[0][0]], a[diferences[1][0]] = a[diferences[1][0]], a[diferences[0][0]]
        if a == b:
            return True
    
    return False
        
        


if __name__ == '__main__':
    a = [1, 2, 2]
    b = [2, 2, 2]
    result = sol(a, b)
    print(result)