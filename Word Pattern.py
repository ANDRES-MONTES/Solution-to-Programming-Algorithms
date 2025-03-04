def wordPattern(pattern: str, s: str) -> bool:
    pattern = list(pattern)
    s = s.split(' ')
    
    if len(pattern) != len(s):
        return False
    
    patron_palabra = {}
    palabra_patron = {} 
    
    for i in range(len(pattern)):        
        if (pattern[i] not in patron_palabra):
            patron_palabra[pattern[i]] = s[i]
        
        if (s[i] not in palabra_patron):
            palabra_patron[s[i]] = pattern[i]
                
        
        if patron_palabra[pattern[i]] == s[i] and palabra_patron[s[i]] == pattern[i]:
            continue
        else:
            return False
        #{a:dog, s:dog }
        #{dog:a, dog:b}
    
    return True
        
            
if __name__ == '__main__':
    pattern = "bsbb"
    s = "dog dog dog dog"
    result = wordPattern(pattern, s)
    print(result)