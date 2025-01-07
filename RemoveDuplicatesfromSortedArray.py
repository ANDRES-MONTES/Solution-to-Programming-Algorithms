def removeDuplicates(nums: list[int]) -> int:
    values = list(set(nums))
    values.sort()
    k = len(values)
    nums[:k +1] = values
    print(nums)
    return k
     


if __name__ == '__main__':
    nums:list[int] = [0,0,1,1,1,2,2,3,3,4]
    result = removeDuplicates([-1,0,0,0,0,3,3])
    print(result)