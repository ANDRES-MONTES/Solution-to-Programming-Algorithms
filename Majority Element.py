def majorityElement(nums: list[int]) -> int:
    val = nums[0]   
    count = 1
    for i in range(1, len(nums)):
        if count == 0:
            val = nums[i]
        
        count += 1 if nums[i] == val else - 1
    
    return val
    
    

if __name__ == '__main__':
    nums = [2, 2, 2, 2, 3, 3, 3,]
    result = majorityElement(nums)
    print(result)
    print(701%26)
