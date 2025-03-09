def reverseString(s: list[str]) -> None:
    vowels = 'AEIOUaeiou'
    s = list(s)
    # data = [i for i in s if i in vowels]    
    # return ''.join([data.pop() if i in vowels else i for i in s])
    i, j = 0, len(s) - 1
    left , right = None, None

    while i < j:
        if s[i] in vowels:
            left = s[i]
        else:
            i += 1
        
        
        if s[j] in vowels:
            right = s[j]
        else:
            j -= 1
            
        
        if left and right:
            s[i], s[j] = right, left
            right = None
            left = None
            i += 1
            j -= 1
        
    
    return ''.join(s)

     
if __name__ == '__main__':
    s = "IceCreAm"
    result = reverseString(s)
    print(result)
        
        
        