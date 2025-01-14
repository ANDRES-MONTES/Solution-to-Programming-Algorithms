def minDepth(root:object) -> int:
    def deep(root) ->int:
        if not root:
            return 0
        
        if root.left == None and root.right == None:
            return 1
        
        if root.left == None:
            return 1 + deep(root.right)
        
        elif root.right == None:
            return 1 + deep(root.left)
        else:
            return 1 + min(deep(root.right), deep(root.left))
    
    return deep(root)
            
if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    # root = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    # root.right.right.right.right = TreeNode(6)
    
    
    root = TreeNode(-9)                         # Nivel 0
    root.left = TreeNode(-3)                    # Nivel 1 - Izquierdo
    root.right = TreeNode(2)                    # Nivel 1 - Derecho
    root.left.right = TreeNode(4)               # Nivel 2 - Derecho de -3
    root.right.left = TreeNode(4)               # Nivel 2 - Izquierdo de 2
    root.right.right = TreeNode(0)              # Nivel 2 - Derecho de 2
    root.left.right.left = TreeNode(-6)         # Nivel 3 - Izquierdo de 4 (en -3)
    root.right.left.right = TreeNode(-5)        # Nivel 3 - Derecho de 4 (en 2)
    
    #root = TreeNode(0)                          # Nivel 0
    # root.left = TreeNode(2)                     # Nivel 1 - Izquierdo
    # root.right = TreeNode(4)                    # Nivel 1 - Derecho
    # root.left.left = TreeNode(1)                # Nivel 2 - Izquierdo de 2
    # root.right.left = TreeNode(3)               # Nivel 2 - Izquierdo de 4
    # root.right.right = TreeNode(-1)             # Nivel 2 - Derecho de 4
    # root.left.left.left = TreeNode(5)           # Nivel 3 - Izquierdo de 1
    # root.left.left.right = TreeNode(1)          # Nivel 3 - Derecho de 1
    # root.right.left.right = TreeNode(6)         # Nivel 3 - Derecho de 3
    # root.right.right.right = TreeNode(8) 

    
    result = minDepth(root)
    print(result)