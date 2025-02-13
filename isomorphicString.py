def isIsomorphic(s: str, t: str) -> bool:
    s, t = list(s), list(t)
    storage = {}
    storage_r = {}
    for i in range(len(s)):
        if s[i] not in  storage:
            storage[s[i]] = t[i]
            
        if t[i] not in storage_r:
            storage_r[t[i]] = s[i]
            
        
        if storage[s[i]] == t[i] and storage_r[t[i]] == s[i]:
            continue
        else:
            return False
    
   
    return True
        
            
            
        
            
        
if __name__ == '__main__':
    s = "add"
    t = "egg"
    result = isIsomorphic(s, t)
    print(set(s))
    print(set(t))
    print('---------------')
    for i in zip(s, t):
        print(i)
    
