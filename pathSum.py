def hasPathSum(root:object, targetSum: int) -> bool:
    if not root:
        return False
    
    def raiz(root, data):
        if not root.right and not root.left:
            data.append(root.val)
            return sum(data) ==  targetSum
        
        if not root.right:
            data.append(root.val)
            return  raiz(root.left, data)
        
        if not root.left:
            data.append(root.val)
            return  raiz(root.right, data)
        
        
        left_path =  raiz(root.left,  data + [root.val])
        right_path = raiz(root.right,  data + [root.val])
        
        
        return left_path or right_path
        
    data= raiz(root, [])
    return data
   
    
    
            
        
        

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
        
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

        
    result = hasPathSum(root, 2)
    print(result)