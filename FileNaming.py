def solution(names:list) -> list:
    for i in range(1, len(names)):
        if names[i] in names[:i]:
           value = 1
           names[i] += f'({value})'
           while names[i] in names[:i]:
               value += 1
               first = names[i].rfind('(')
               last = names[i].rfind(')')
               names[i] = [i for i in names[i]]
               names[i][first + 1: last] = str(value)
               names[i] = ''.join(names[i])
               print(names)
            
    return names
    
            
            
    

if __name__ == '__main__':
    names = ["doc", "doc", "image", "doc(1)", "doc"]
    otro = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
    final = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
    # data =  "dd(1)(13)"
    # first =data.rfind('(')
    # last = data.rfind(')')
    # print(data)
    # data = [i for i in data]
    # data[first + 1: last] = str(100)
    # print([i for i in data][first + 1: last])
    # print(first)
    # print(last)
    # print(''.join(data))
    
    result = solution(names)
    print(result)
