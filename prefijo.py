def longestCommonPrefix(strs:list[str]) -> str:
    if len(strs) == 0 or '' in strs:
        return ''
    
    minimo = len(min(strs, key=lambda x: len(x)))
    result = ''
    for i in range(minimo):
        letter = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] == letter:
                continue
            else:
                return result
        
        result += letter
    
    return result
            
            
if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    # ['abc', 'abcdff', 'abddc']
    result = longestCommonPrefix(strs)
    print(result)

