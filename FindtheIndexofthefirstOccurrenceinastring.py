def strStr(haystack:str, needle:str) -> int:
    i:int = 0
    j:int = len(needle)
    while j <= len(haystack):
        compare:str = haystack[i:j]
        if compare == needle:
            return i
        else:
            i += 1
            j += 1
            
    return -1
        
        
    


if __name__ == '__main__':
    haystack = "dhabuhsadbutsad"
    needle = "sad"
    result = strStr(haystack, needle)
    print(result)