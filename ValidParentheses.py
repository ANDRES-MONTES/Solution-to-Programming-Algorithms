def isValid(s: str) -> bool:
    while True:
        print(s)
        if '()' in s:
            s:str = s.replace('()', '')
        elif '{}' in s:
            s:str = s.replace('{}', '')    
        elif '[]' in s:
            s:str =  s.replace('[]', '')
        else:
            if s:
                return False
            else:
                return True
        
        
                    
if __name__ == '__main__':
    input = "(){()}[]"
    result = isValid('()[}}]')
    print(result) #'([{])'
    