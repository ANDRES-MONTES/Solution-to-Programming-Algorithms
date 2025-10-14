
def getMinimumDifference(root:object) -> int:
    import heapq
    values = []
    stack = []
    pivot = root
    while stack or pivot:
        while pivot:
            stack.append(pivot)
            pivot = pivot.left
        
        valor = stack.pop()
        values.append(valor.val)
        pivot = valor.right
    
    heapq.heapify(values)
    diferrences = []
    for i in range(len(values) - 1):
        diferrences.append(values[i + 1] - values[i])
    
    return min(diferrences)    
    

if __name__ == '__main__':
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    result = getMinimumDifference(tree)
    print(result)
    
        