def sol(n):
    import re
    result = re.match(r'^[^\d -\.][\w ]*$', n)
    if result:
        return True
    
    return False
    


if __name__ == '__main__':
        val = 'va[riable0' 
        result = sol(val)
        print(result)
