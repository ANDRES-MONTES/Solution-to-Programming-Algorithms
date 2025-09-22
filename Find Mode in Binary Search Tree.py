def findMode(root:object) -> list[int]:
    from collections import Counter
    stack = []
    data = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        val = stack.pop()
        data.append(val.val)
        current = val.right
    
    comun = Counter(data).most_common()
    vals = list(map(lambda x: x[0], filter(lambda x:x[1] == comun[0][1],comun)))
    return vals


if __name__ == '__main__':
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    arbol = TreeNode(val=1, right=TreeNode(2, left=TreeNode(val=2)))
    result = findMode(TreeNode(0))
    print(result)