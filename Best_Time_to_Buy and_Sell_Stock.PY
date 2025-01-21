def maxProfit(prices: list[int]) -> int:
    max_return = 0
    min_val = prices[0]
    
    for i in prices[1:]:
        min_val = min(min_val, i)
        profit =  i - min_val
        max_return = max(profit, max_return)
        print(min_val, profit, max_return)
    
    return max_return
        
    
    
          

if __name__ == '__main__':
    Input = [7,1,5,3,6,4]
    Output=  5
    result = maxProfit(Input)
    print(result)