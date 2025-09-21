def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    data = []
    esta = False
    for i in nums1:
        position = nums2.index(i)
        for j in range(position + 1, len(nums2)):
            if nums2[j] > i:
                data.append(nums2[j])
                esta = True
                break
    
        if esta:
            esta = False
        else:
            data.append(-1)
        
    return data

if __name__ == '__main__':
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    result = nextGreaterElement(nums1, nums2)
    print(result)
        