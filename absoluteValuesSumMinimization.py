def sol(n:list):
    values = []
    for i in range(len(n)):
        amount = 0
        for j in range(len(n)):
            amount += abs(n[i] - n[j])
        values.append((n[i], amount))
    
    print(values)
    minimo = min(values, key=lambda x:x[1])[0]
    return minimo



if __name__ == '__main__':
    data = [2, 4, 7]
    result = sol(data)
    print(result)