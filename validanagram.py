def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    vals = set(s)
    for i in vals:
        if s.count(i) != t.count(i):
            return False
    
    return True
    
    
    
    
   
if __name__ == '__main__':
    s = "anagrhm"
    t = "nagarav"
    result = isAnagram(s, t)
    print(result)