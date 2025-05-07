def findMaxConsecutiveOnes(nums: list[int]) -> int:
    #return len(max(''.join([str(i) for i in nums]).split('0'), key=len))
    maximo = 0
    current = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            current += 1
        else:
            maximo = max(maximo, current)
            current = 0
    
    maximo = max(maximo, current)
    return maximo
    
    
    
if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    result = findMaxConsecutiveOnes(nums)
    print(result)