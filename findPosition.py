def searchInsert(nums: list[int], target: int) -> int:
    try:
        return  nums.index(target)
    except:
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            else:
                return i
            
        return len(nums)
        




if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    result = searchInsert(nums, target)
    print(result)