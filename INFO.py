

def sol(data:str):
    info = [x for x in data]
    i = 0
    print(info)
    while i < len(info):
        first = 0
        if info[i] == '(':
            first += int(i)
            i += 1
        break
    


if __name__ == '__main__':
    data = 'foo(bar)baz(blim)'
    data_1 = 'foo(bar(ba)zb)lim'
    result = sol(data_1)
    print(result)

    