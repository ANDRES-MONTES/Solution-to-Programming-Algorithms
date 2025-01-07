def solution(address):
    address = address[::-1]
    info = ''
    for i in range(len(address)):
        if address[i] == '@':
            break
        info += address[i]
    
    return info[::-1]

    import re
    result = re.search(r'@[^@]*$', address)
    return result.group()[1:]

    





if __name__ == '__main__':
    val1 =  "\"very.unusual.@.unusual.com\"@usual.com"  
    val2 = "prettyandsimple@example.com"
    result = solution(val1)
    print(result)