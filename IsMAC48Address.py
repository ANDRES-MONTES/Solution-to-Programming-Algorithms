def solution(inputString):
    import re
    result = re.match(r'((\d[ABCDEF]|\d\d|[ABCDEF][ABCDEF]|[ABCDEF]\d)-){5,5}([ABCDEF]{2,2}$|\d\d$|\d[ABCDEF]$|[ABCDEF]\d$)', inputString)    
    if result:
        return True
    else:
        return False
if __name__ == '__main__':
    data = "00-00-00-00-00-00"
    result = solution(data)
    print(result)
    