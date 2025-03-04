def moveZeroes(nums: list[int]) -> None:
    counter = 0
    i = 0
    while counter < len(nums):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
        else:
            i += 1
        
        counter += 1
    


    
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    result = moveZeroes([0, 0, 1])