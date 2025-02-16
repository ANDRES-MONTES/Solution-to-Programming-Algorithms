
def invertTree(root:object) -> object:
    if root.left == None and root.right == None:
        return root
    
    
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    
    
    
    return root
    
    

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    result = invertTree(root)
    print(result.val)
    print(result.left.val)
    print(result.left.left.val)
    print(result.left.right.val)
    
    print(result.right.val)
    print(result.right.left.val)
    print(result.right.right.val)
    
    