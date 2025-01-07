def isPalindrome(x: int) -> bool:
        x =[i for i in str(x)]
        z = 0
        y = len(x) - 1
        
        while z < y:
            if x[z] == x[y]:
                z += 1
                y -= 1
            else:
                return False
        return True
        
            
                
                
            

if __name__ == '__main__':
    nums = 121
    result = isPalindrome(nums)
    print(result)