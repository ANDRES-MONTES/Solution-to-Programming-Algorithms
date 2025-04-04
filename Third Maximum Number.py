def thirdMax(nums:list[int]) -> int:
    result = 0
    nums = set(nums)
    
    if len(nums) == 2:
        return max(nums)
    
    for _ in range(3):
        result = max(nums)
        nums.remove(result)
    
        
        
    return result


if __name__ == '__main__':
    nums = [2,1,3, 5]
    result = thirdMax(nums)
    print(result)