def sol(arr:list):
    result = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            continue
        else:
            meta = arr[i] + 1
            steps = abs(meta - arr[i +  1])
            result += steps
            arr[i + 1] = meta
            
    return result



if __name__ == '__main__':
    nputArray = [-1000, 0, -2, 0]
    result = sol(nputArray)
    print(result)