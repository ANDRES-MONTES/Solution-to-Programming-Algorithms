def solution(p:object, q:object) -> bool:
    if p and q:
        stack_1, stack_2 = [], []
        val_1, val_2 = [], []
        pivot_1, pivot_2 = p, q
        
        while (stack_1 or pivot_1) or (stack_2 or pivot_2):
            while pivot_1 or pivot_2:
                if pivot_1 and pivot_2:
                    if pivot_1.val == pivot_2.val:
                        pass
                    else:
                        return False
                else:
                    return False
                
                if pivot_1.left and pivot_2.left:
                    stack_1.append(pivot_1)
                    stack_2.append(pivot_2)
                    pivot_1 = pivot_1.left
                    pivot_2 = pivot_2.left
                        
                elif pivot_1.left or pivot_2.left:
                    return False
                else:
                    stack_1.append(pivot_1)
                    stack_2.append(pivot_2)
                    break
            
            num_1 = stack_1.pop()
            num_2 = stack_2.pop()
            
            val_1.append(num_1.val)
            val_2.append(num_2.val)
            
            pivot_1 = num_1.right
            pivot_2 = num_2.right
            
        
        if val_1 == val_2:
            return True
        
        return False
    
    if p or q:
        return False
    else:
        return True

            
            
if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    arbol = TreeNode(1)
    # arbol.left.right = TreeNode(1)
    # arbol.left.right.left = TreeNode(2)
    # arbol.right.right = TreeNode(4)
    # arbol.right.right.left = TreeNode(2)
    
    
    # arbol_3 = TreeNode(5, TreeNode(4), TreeNode(1))
    # arbol_3.left.right = TreeNode(1)
    # arbol_3.left.right.left = TreeNode(2)
    # arbol_3.right.right = TreeNode(4)
    # arbol_3.right.right.left = TreeNode(2)
    
    arbol_2 = TreeNode(1, right=TreeNode(2))
    # arbol_2.left.left = TreeNode(4)
    # arbol_2.left.left.right = TreeNode(2)
    # arbol_2.right.left = TreeNode(1)
    # arbol_2.right.left.right = TreeNode(2)
    
    arbol_3 = None
    
    

    
    
    
    
    result = solution(arbol, arbol_2)
    print(result)