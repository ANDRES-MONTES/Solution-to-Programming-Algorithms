def hammingDistance(x: int, y: int) -> int:
    print(bin(x)[2:])
    print(bin(y)[2:])
    
    x = list(bin(x)[2:])
    y = list(bin(y)[2:])
    
    if len(y) > len(x):
        for _ in range(abs(len(y) - len(x))):
            x.insert(0, '0')

    elif len(x) > len(y):
        for _ in range(abs(len(y) - len(x))):
            y.insert(0, '0')

    hammin = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            hammin += 1
            
    return hammin    
 

if __name__ == '__main__':
    x = 680142203
    y = 1111953568
    result = hammingDistance(x, y)
    print(result)