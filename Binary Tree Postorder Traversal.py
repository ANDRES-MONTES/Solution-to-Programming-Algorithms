def postorderTraversal(root:object) -> list[int]:
    data = []
    stack = []
    pivot = root
    again = []
    
    while stack or pivot:
        while pivot:
            stack.append(pivot)
            pivot = pivot.left
        
        last = stack[-1]
        again.append(last)
        
        if not again.count(last) == 2:
            pivot = last.right
        
        if again.count(last) == 2:
            data.append(last.val)
            stack.pop()
                 
        elif not pivot:
           data.append(last.val)
           stack.pop()
    
    return data
    
    

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    root = TreeNode(1)  # Nodo raíz
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # Subárbol izquierdo
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Subárbol derecho
    root.right.right = TreeNode(8)

    # Hijos de root.left.right
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)

    # Hijo de root.right.right
    root.right.right.left = TreeNode(9)
    
    result = postorderTraversal(root)
    print(result)