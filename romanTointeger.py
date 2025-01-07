def solution(s:str) -> int:
    info = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
   
    amount = sum([info[i] for i in s])
    for i in range(len(s)- 1):
        if info[s[i]] < info[s[i + 1]]:
            amount -= info[s[i]] * 2
        
    return amount



if __name__ == '__main__':
    input = 'IVI'
    result = solution(input)
    print(result)
    