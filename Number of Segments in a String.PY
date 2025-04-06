def countSegments(s: str) -> int:
    import re
    print(re.findall(r'\S+', s))
    return len(re.findall(r'\S+', s))
    


if __name__ == '__main__':
    s =  "love live! mu'sic forever"
    result = countSegments(s)
    print(result)
