def sumOfLeftLeaves(root:object) -> int:
    data = []
    def wrap(root):
        if not root:
            return
        
        if root.left:
            if root.left.left == None and root.left.right == None:
                data.append(root.left.val)
        
        wrap(root.left)
        wrap(root.right)

    wrap(root)
    print(data)
    return sum(data)
            

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    root = TreeNode(3, TreeNode(9, TreeNode(8)), TreeNode(20, TreeNode(15), TreeNode(7, TreeNode(11))))
    result = sumOfLeftLeaves(root)
    print(result)