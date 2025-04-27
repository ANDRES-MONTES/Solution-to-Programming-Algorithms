def findDisappearedNumbers(nums: list[int]) -> list[int]:
    datos = set(nums)
    result = []
    for i in range(1, len(nums)+1):
        if i not in datos:
            result.append(i)
    return result
        
   
    
if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    result = findDisappearedNumbers(nums)
    print(result)