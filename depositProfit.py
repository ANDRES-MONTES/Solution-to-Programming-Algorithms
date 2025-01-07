def sol(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        increase = (deposit * rate) / 100
        deposit += increase
        year += 1
        print(deposit)
        
    return year


if __name__ == '__main__':
     deposit = 100
     rate = 1
     threshold = 101
     result = sol(deposit, rate, threshold)
     print(result)