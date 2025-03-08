class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        value = self.nums[left:right + 1]
        return sum(value)
    
    
arr = NumArray([-2, 0, 3, -5, 2, -1])
print(arr.sumRange(0, 5))
