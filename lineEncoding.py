def solution(s:str) -> str:
    s = list(s) #"aabbbc"
    save = []
    current = s[0]
    data = ''
    data += s[0]
    for i in range(1, len(s)):
        if s[i] == current:
            data += s[i]
            if i == len(s) - 1:
                save.append(data)
        else:
            save.append(data)
            data = ''
            current = s[i]
            data += s[i]
            if i == len(s) - 1:
                save.append(data)
    
    print(save)
    save = [f'{i[0]}' if len(i) == 1 else f'{len(i)}{i[0]}' for i in save]
    return ''.join(save)

                    
if __name__ == '__main__':
    info = "aabbbc"
    result = solution(info)
    print(result)