def arrangeCoins(n: int) -> int:
    # num_rows = 0
    # num_monedas = 1
    # aumento = 2
    # while num_monedas <= n:
    #     num_rows += 1
    #     num_monedas += aumento
    #     aumento += 1
        
    # return num_rows
    
    return int((-1 + (1 + 8 * n) ** 0.5) / 2)
    
        

if __name__ == '__main__':
    n = 8
    result = arrangeCoins(n)
    print(result)