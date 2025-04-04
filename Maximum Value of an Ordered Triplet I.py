def maximumTripletValue(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                result = max((nums[i] - nums[j]) * nums[k], result)
                print(result)
        
    return result
        
    

if __name__ == '__main__':
    nums = [1,10,3,4,19]
    result = maximumTripletValue(nums)
    print(result)