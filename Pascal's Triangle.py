def generate(numRows: int) -> list[list[int]]:
    result = []
    for i in range(1, numRows + 1):
        if i == 1 or i ==2:
            if i== 1:
                result.append([1])
            if i == 2:
                result.append([1, 1])
        else:
            pivot = result[-1]
            val = [1]
            for i in range(len(pivot) - 1):
                val.append(sum(pivot[i:i+2]))
            val.append(1)
            result.append(val)
                
                
    return result


if __name__ == '__main__':
    num_rows:int=8
    result = generate(num_rows) 
    print(result)