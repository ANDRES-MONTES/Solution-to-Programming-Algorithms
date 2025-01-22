def isPalindrome(s: str) -> bool:
    import re
    values = [i.lower() for i in re.findall(r'[^\W_]+', s)]
    print(values)
    messaje = ''.join(values)
    
    if messaje == messaje[::-1]:
        return True
    
    return False


if __name__ == '__main__':
    s = "PANAMA ACA EN CA_SA: PANAMA"
    resuult = isPalindrome(s)
    print(resuult)
    print(int('000', 2))