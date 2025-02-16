
def countNodes(root:object) -> int:
    stack = []
    nodos = []
    pivot = root
    
    while pivot or stack:
        while pivot:
            stack.append(pivot)
            pivot = pivot.left
        
        val = stack.pop()
        nodos.append(val)
        pivot = val.right
    
    return len(nodos)


if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    result = countNodes(None)
    print(result)
        