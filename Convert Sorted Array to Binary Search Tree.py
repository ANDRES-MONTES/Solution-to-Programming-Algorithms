def solution(nums:list[int]) -> object:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    if not nums:
        return
            
    mitad= int(len(nums) / 2)
    cabeza = nums[mitad]
    izquierda = nums[:mitad]
    derecha = nums[mitad +1:]
    
    return TreeNode(cabeza, right=solution(derecha), left=solution(izquierda))
    
 
if __name__ == '__main__':
    data = solution( [-10, -3, 0, 5, 9])
    print(data.val)
    print(data.left.val)
    print(data.left.left.val)
    print(data.right.val)
    print(data.right.left.val)
    
    
    
    
    