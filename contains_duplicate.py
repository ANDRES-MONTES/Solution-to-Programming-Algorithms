def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    data = {}
    for i, j in enumerate(nums):
        if j in data and abs(data[j] - i) <= k:
            return True
        
        data[j] = i
    
    return False
        
        
            
        
    


if __name__ == '__main__':
    nums = [1,0,1,1, 0]
    k = 2
    result = containsNearbyDuplicate(nums, k)
    print(result)
    print(list(enumerate(nums)))
 