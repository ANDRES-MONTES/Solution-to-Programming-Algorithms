def sol(n, first_number):
    circulo = [i for i in range(n)]
    mitad = len(circulo) // 2
    print(circulo, mitad)

    i = 1
    while i <= first_number:
        if mitad == len(circulo) - 1:
            mitad = 0
            i += 1
            continue
        
        mitad += 1
        i += 1

    return mitad
        


if __name__ == '__main__':
    n = 20
    first = 2
    result = sol(n, first)
    print(result)