def removeElement(nums: list[int], val: int) -> int:
    k = len(nums) - nums.count(val)
    for i in range(len(nums)):
        if nums[i]== val:
            save = nums[i]
            nums.remove(nums[i])
            nums.append(save)
    print(nums)
    return k



if __name__ =='__main__':
    Input = [0,1,2,2,3,0,4,2]
    val = 2
    result = removeElement(Input, val)
        