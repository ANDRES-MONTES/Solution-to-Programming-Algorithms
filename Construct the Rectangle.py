def constructRectangle(area: int) -> list[int]:
    i = round(area**(1/2))
    while area % i != 0:
        i -= 1
    
    j = int(area / i)
    val = [i, j]
    val.sort(reverse=True)
    return val
        

if __name__ == '__main__':
    area = 122122
    result = constructRectangle(area)
    print(result)