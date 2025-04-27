def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    for i in range(1, n//2 + 1):
        if n % i == 0:
            substring = s[:i]
            if substring * (n // i) == s:
                return True
            
    return False
        
   
        

if __name__ == '__main__':
    s = "aba"
    result = repeatedSubstringPattern(s)
    print(result)
