def solution(root:object) -> int:
    if not root:
        return 0
    
    fila = []
    pivot = root    
    fila.append([pivot])
    i = 0
    while i == len(fila) - 1:
        data = []
        for j in range(len(fila[i])):
            if fila[i][j].left:
                data.append(fila[i][j].left)
            if fila[i][j].right:
                data.append(fila[i][j].right)
        if data:
            fila.append(data)
            i += 1
        else:
            i += 1
    
    return len(fila)
                


if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    Tree = TreeNode(3, TreeNode(20), TreeNode(9))
    Tree.right.left = TreeNode(15)
    Tree.right.right = TreeNode(7)
    
    result = solution(None)
    print(result)
    