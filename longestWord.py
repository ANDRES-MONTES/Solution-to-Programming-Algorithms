def solution(text):
    import re 
    info = re.findall(r'[A-Za-z]+', text)
    data = [(len(i), i) for i in info]
    return max(data, key=lambda x : x[0])[1]
    
    
    
if __name__ == '__main__':
    text = "To be or not to be"
    
    result = solution(text)
    print(result)