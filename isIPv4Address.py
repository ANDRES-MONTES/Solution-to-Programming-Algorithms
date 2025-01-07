def solution(ip:str):
    data = ip.split('.')
    print(data)
    
    if len(data) != 4:
        return False
    
    for i in range(len(data)):
        if data[i] == '':
            return False
        try:
            if int(data[i]) < 0 or int(data[i]) > 255:
                return False
            elif len(data[i]) > 1 and data[i][0] == '0':
                return False
        except:
            return False
        
    return True
            
            
    
    
    
if __name__ == '__main__':
   ip = "1.1.1.1a"
   result =  solution(ip)
   print(result)
