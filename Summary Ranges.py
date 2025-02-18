def summaryRanges(nums: list[int]) -> list[str]:
    vals = []
    first = None
    last = None
    
    if len(nums) == 1:
        return [str(nums[0])]
    
    for i in range(len(nums) - 1):
        if not first:
            first = str(nums[i])
            
        if abs(nums[i] - nums[i + 1]) != 1:
            last = str(nums[i])
            if first == last:
                rango = first            
            else:
                rango = first+'->'+last
            
            vals.append(rango)
            first = None
            last = None
        
        if i + 2 == len(nums):
            if not first:
                rango = str(nums[i + 1])
            else:
                rango = f'{first}->{nums[i + 1]}'
                
            vals.append(rango)
            
        

    return vals
    
    
    

if __name__ == '__main__':
    ums = [0,2,3,4,6,8,9]
    Output =  ["0","2->4","6","8->9"]
    result = summaryRanges([0,1,2,4,5,7])
    print(result)
