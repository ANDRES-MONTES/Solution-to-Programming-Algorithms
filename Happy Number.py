def isHappy(n: int) -> bool:
    from functools import reduce
    num = [int(i) for i in list(str(n))]
    stack = []
    
    while n != 1:
        data = reduce(lambda x, y: x + y **2 , num, 0)
        n = data
        stack.append(data)
        num = [int(i) for i in list(str(data))]
        
        if stack.count(data) == 2:
            return False
     

    return True

if __name__ == '__main__':
    n = 18
    result = isHappy(n)
    print(result)