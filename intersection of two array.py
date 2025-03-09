def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    from collections import Counter
    contador = Counter(nums1)
    print(contador)
    data = []
    for i in range(len(nums2)):
        if nums2[i] in contador and contador[nums2[i]] > 0:
            data.append(nums2[i])
            contador[nums2[i]] -= 1
    
    return data
            
         

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    result = intersection(nums1, nums2)
    re = intersect(nums1, nums2)
    print(re)