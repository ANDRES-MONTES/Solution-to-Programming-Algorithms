def lengthOfLastWord(s: str) -> int:
    i:int = 0
    words:list[str] = []
    while i < len(s):
        if s[i] == ' ':
            i+= 1
        else:
            word:str = ''
            while  i < len(s) and s[i] != ' ' :
                word += s[i]
                i += 1
                
            words.append(word[:])
        
    return len(words[-1]) 
            


if __name__ =='__main__':
    Input = "   fly me   to   the moon  "
    result = lengthOfLastWord(Input)
    print(result)
