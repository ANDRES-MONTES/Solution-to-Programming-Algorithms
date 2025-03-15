def isSubsequence(s: str, t: str) -> bool:
    import collections
    data = collections.defaultdict(list)
    for i in range(len(t)): data[t[i]].append(i)
    data = dict(data)
    
    indice = []
    for i in range(len(s)):
        if s[i] not in data:
            return False
        else:
            j = 0
            if i == 0:
                indice.append(data[s[i]][0])
            else:
                while j < len(data[s[i]]):
                    if data[s[i]][j] <= indice[-1]:
                        j += 1
                    else:
                        indice.append(data[s[i]][j])
                        break

    if len(indice) == len(s):
        return True
    
    return False
                
                        
                
if __name__ == '__main__':
    s = "aaaaaa" 
    t = "bbaaaa"
    result = isSubsequence(s, t)
    print(result)
