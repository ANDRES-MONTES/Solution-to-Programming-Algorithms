def canConstruct(ransomNote: str, magazine: str) -> bool:
    for i in range(len(ransomNote)):
        if ransomNote[i] in magazine:
            print(magazine)
            magazine = magazine.replace(ransomNote[i], '', 1)
        else:
            return False
        
    return True
    
    
   
if __name__ == '__main__':
     ransomNote = "aa"
     magazine = "aab"
     result = canConstruct(ransomNote, magazine)
     print(result)
     

