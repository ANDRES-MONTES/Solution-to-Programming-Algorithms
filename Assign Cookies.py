def findContentChildren(g:list[int], s:list[int]) -> int:
    g.sort()
    s.sort()
    i, j = 0, 0
    maximaze = 0
    
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            maximaze += 1
            i += 1
            j += 1
        else:
            i += 1
            
    return maximaze
            
if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1,1]
    result = findContentChildren(g, s)
    print(result)