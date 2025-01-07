"""
En el taller de Santa, los elfos aman los acertijos 🧠. Este año, han creado uno especial: un desafío para formar un palíndromo navideño.

Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás. Los elfos quieren saber si es posible formar un palíndromo haciendo, como mucho, un intercambio de letras.

Crea una función getIndexsForPalindrome que reciba una cadena de caracteres y devolverá:

Si ya es un palíndromo, un array vacío.
Si no es posible, null.
Si se puede formar un palíndromo con un cambio, un array con las dos posiciones (índices) que se deben intercambiar para poder crearlo.
Por ejemplo:

getIndexsForPalindrome('anna') // []
getIndexsForPalindrome('abab') // [0, 1]
getIndexsForPalindrome('abac') // null
getIndexsForPalindrome('aaaaaaaa') // []
getIndexsForPalindrome('aaababa') // [1, 3]
getIndexsForPalindrome('caababa') // null
Si se puede formar el palíndromo con diferentes intercambios, siempre se debe devolver el primero que se encuentre.
"""


def get_indexs_for_palindrome(word:str):
    result = None
    if word == word[::-1]:
        result = []
        
    else:
        review = [x for x in word]
        veces = len(review) - 1
        for i in range(len(review) - 1):
            iter = 1
            for j in range(veces):
                change = review.index(review[i + iter])
                review[i], review[i + iter] = review[i + iter], review[i]
                info = ''.join(review)
                #print(info)
                
                if info == info[::-1]:
                     result = [i, change]
                     return result
                else:
                    review[i + iter], review[i] = review[i], review[i + iter]
                    iter += 1
            veces -= 1


    return result




if __name__ == '__main__':
    word = 'aaababa'
    result = get_indexs_for_palindrome(word)
    print(result)