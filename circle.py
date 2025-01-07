def solution(n, firstNumber):
    circle = [i for i in range(n)]
    mitad = len(circle) // 2
    indice = circle.index(firstNumber)
    if indice >= mitad:
        contrario  = indice - mitad
        return circle[contrario]
    else:
        contrario = indice + mitad
        return circle[contrario]


if __name__ == '__main__':
    n = 10
    firstNumber = 7
    result = solution(n, firstNumber)
    print(result)