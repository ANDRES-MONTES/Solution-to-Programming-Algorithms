def solution(tree:object) -> bool:
    if tree.left == None and tree.right == None:
        return True
    
    stack, values= [], []
    pivot = tree
    rigths = 0
    lefts = 0
    
    while stack or pivot:
        while pivot:
            if pivot.left:
                lefts += 1
            stack.append(pivot)
            pivot = pivot.left
        
        value = stack.pop()
        values.append(value.val)
        if value.right:
            rigths += 1
        pivot = value.right

    if len(values) % 2 == 0:
        return False
    else:
        if rigths == lefts:
            if tree.left.val == tree.right.val:
                mitad = int((len(values) - 1) / 2)
                first = values[:mitad]
                last = values[mitad + 1:]
                if first == last[::-1]:
                    return True
                
                return False
            return False
            
        return False

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    tree_1 = TreeNode(1, TreeNode(2), TreeNode(2))
    tree_1.left.left = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right.left = TreeNode(4)
    tree_1.right.right = TreeNode(3)
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(1)

    root.left.right = TreeNode(1)
    root.right.right = TreeNode(4)

    root.left.right.left = TreeNode(2)
    root.right.right.left = TreeNode(2)
        
    result = solution(TreeNode)
    print(result)

    
            
            