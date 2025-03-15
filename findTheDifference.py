def findTheDifference(s: str, t: str) -> str:
    for i in s:
        t = t.replace(i, '', 1)
        
    return t


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    result = findTheDifference(s, t)
    print(result)