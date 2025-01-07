def solution(text):
    text = [x for x in text if x]
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '_':
            text[i + 1] = text[i + 1].upper()
            
    text = [x for x in text if x != '-' and x != '_']
    return ''.join(text)
   
   
   
print(solution('the-stealth-warrior'))