def merge(nums1:list[int], m: int, nums2: list[int], n: int) -> None:
    del nums1[m:]
    for i in range(n):
        nums1.append(nums2[i])
    
    nums1.sort()

     
   

    
if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    result = merge(nums1, m, nums2, n)
    print(result)
    
        