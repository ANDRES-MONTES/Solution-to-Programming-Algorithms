def licenseKeyFormatting(s: str, k: int) -> str:
    s = s.replace('-', '').upper()[::-1]
    return '-'.join([s[i:i+k] for i in range(0, len(s), k)])[::-1]
    
    
    
    
    # agrupados = s[::-1]
    # result = ''
    # current = ''
    # for i in range(len(agrupados)):
    #     if agrupados[i] != '-' and len(current) <= k:
    #         current += agrupados[i]
            
    #         if len(current) == k and i != len(agrupados) - 1:
    #             result += current
    #             result += '-'
    #             current = ''
                
    #     if i == len(agrupados) - 1 and len(current) > 0:
    #         result += current
            
    # result = result.upper()[::-1]
    # if result and result[0] == '-':
    #     result = result.replace('-', '', 1)

    # return result
            
    
if __name__ == '__main__':
    s =  "2-5g-3-J"
    k = 2
    result = licenseKeyFormatting(s, k)
    print(result)
