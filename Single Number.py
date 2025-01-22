def singleNumber(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        result ^= nums[i]
        
    return result


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    result = singleNumber(nums)
    print(0 ^ 0)