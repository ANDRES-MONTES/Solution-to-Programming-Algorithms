def solution(inputString:str) -> int:
    import re
    info = re.findall(r'\d+', inputString)
    info = [int(i) for i in info]
    return sum(info)


if __name__ == '__main__':
    inputString = "2 apples, 12 oranges"
    result = solution(inputString)
    print(result)
