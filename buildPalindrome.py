def solution(st:str):
    if st == st[::-1]:
        return st
    
    st = [i for i in st]
    stR = st[::-1] 
    print(st, stR)
    i = -1  
    
    for _ in range(len(st)):
        pivot = st + stR[i:]
        print(pivot)
        if pivot == pivot[::-1]:
            return ''.join(pivot)
        else:
            i -= 1
                
      
            
       

if __name__ == '__main__':
    st = "abcdc" #abaaba
    result = solution(st)
    print(result)
    'abcdcdcba'