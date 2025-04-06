def addStrings(num1: str, num2: str) -> str:    
    import sys
    sys.set_int_max_str_digits(10000)
    return str(int(num1) + int(num2))
    
            
if __name__ == '__main__':
    num1 = "1"
    num2 = "99"
    result = addStrings(num1, num2)
    print(result)
