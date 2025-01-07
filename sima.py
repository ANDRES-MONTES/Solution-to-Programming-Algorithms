def sol(a:list):
    ancho = len(a[0]) + 2
    result = []
    result.append('*' * ancho)
    for i in range(len(a)):
        value = f'*{a[i]}*'
        result.append(value)
    
    result.append('*' * ancho)
    return result
   


if __name__ == '__main__':
    a = ["abcde", 
 "fghij", 
 "klmno", 
 "pqrst", 
 "uvwxy"]
    result = sol(a)
    for i in result:
        print(i)