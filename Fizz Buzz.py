def fizzBuzz(n: int) -> list[str]:
    result = []
    for i in range(1 , n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            result.append('FizzBuzz')
        elif (i % 3 == 0):
            result.append('Fizz')
        elif (i % 5 == 0):
            result.append('Buzz')
        else:
            result.append(i)
            
    return result
            

if __name__ == '__main__':
    n = 15
    result = fizzBuzz(n)
    print(result)
