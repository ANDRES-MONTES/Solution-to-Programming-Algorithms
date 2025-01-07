def solustion(root:object) -> list[int]:
    stack = []
    result = []
    pivot = root
    
    while stack or pivot:
        while pivot:
            stack.append(pivot)
            if pivot.left:
                pivot = pivot.left
            else:
                break
            
        valor = stack.pop()
        result.append(valor.val)
        pivot = valor.right

    return result



if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    arbol = TreeNode(1, TreeNode(2), TreeNode(3))
    arbol.left.left = TreeNode(4)
    arbol.left.right = TreeNode(5)
    arbol.left.right.left = TreeNode(6)
    arbol.left.right.right = TreeNode(7)
    arbol.right.right = TreeNode(8)
    arbol.right.right.left = TreeNode(9)
    
    result = solustion(arbol)
    print(result)
    
    
    
    