def solution(root:object) -> bool:
    def aplanar_arbol(arbol:object)-> list:
        stack = []
        data = []
        pivot = arbol
        
        while pivot or stack:
            while pivot:
                stack.append(pivot)
                pivot = pivot.left
            
            nodo = stack.pop()
            data.append(nodo)
            pivot = nodo.right
        
        return data
        
    def deep(nodo:object) -> int:
        if not nodo:
            return 0
        
        deep_derecha = deep(nodo.right)
        deep_izquierda = deep(nodo.left)
        
        return 1 + max(deep_derecha, deep_izquierda)
    
    
    data = aplanar_arbol(root)
    for i in range(len(data)):
        derecha = deep(data[i].right)
        izquierda = deep(data[i].left)
        
        if abs(derecha - izquierda) > 1:
            return False
        
    return True
    
    
    
    
if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    # root = TreeNode(3)
    # root.left = TreeNode(9)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(7)
    
    
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.left.left.left = TreeNode(4)
    # root.left.right.left = TreeNode(4)
    
    # Construcción del árbol
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)

    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(3)
    # root.right.right = TreeNode(3)

    # root.left.left.left = TreeNode(4)
    # root.left.left.right = TreeNode(4)
    # root.left.right.left = TreeNode(4)
    # root.left.right.right = TreeNode(4)
    # root.right.left.left = TreeNode(4)
    # root.right.left.right = TreeNode(4)
    # root.right.right.left = TreeNode(4)
    # root.right.right.right = TreeNode(4)

    # root.left.left.left.left = TreeNode(5)
    # root.left.left.left.right = TreeNode(5)
    
    
    # Creación de los nodos
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    # Nivel 2
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)

    # Nivel 3
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(4)

    root.right.left.left = TreeNode(4)
    root.right.left.right = TreeNode(4)
    root.right.right.left = None
    root.right.right.right = None

    # Nivel 4
    root.left.left.left.left = TreeNode(5)
    root.left.left.left.right = TreeNode(5)
    
    result = solution(TreeNode(1))
    
    
    print(result)