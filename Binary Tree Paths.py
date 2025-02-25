def binaryTreePaths(root:object) -> list[str]:
    rangos = []
    def ramas(nodo, rama) ->str:
        rama.append(nodo.val)
        
        if nodo.left == None and nodo.right == None:
            ram = "->".join(map(str, rama))
            rangos.append(ram)
            return
        
        if nodo.right:
            ramas(nodo.right, rama[:])
        
        if nodo.left:
            ramas(nodo.left, rama[:])
            
    
    ramas(root, [])
    return rangos
   
            
        
           
    
if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    root = TreeNode(1, TreeNode(2, right=TreeNode(5)), TreeNode(3))
    root_2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    
    result = binaryTreePaths(root)
    print(result)

    
