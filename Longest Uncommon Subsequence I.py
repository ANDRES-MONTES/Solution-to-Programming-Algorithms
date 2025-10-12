def findLUSlength(a: str, b: str) -> int:
    if a == b:
        return -1
    
    return len(max(a, b, key=len))
        
        

if __name__ == '__main__':
    a = "aefawfawfawfaw"
    b = "aefawfeawfwafwaef"
    result = findLUSlength(a, b)
    print(result)