def missingNumber(nums: list[int]) -> int:
    nums.sort()
    if nums[0] != 0:
        return 0
    
    for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) == 1:
                continue
            else:
                return nums[i] + 1
            
    return nums[-1] + 1
     


if __name__ == '__main__':
    nums = [9,6,4,2,3,5,7,0,1]
        #1, 2, 3, 4, 5, 6, 7, 9
    result = missingNumber([2])
    print(result)
    