"""¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que sea especial. Vamos a crear una función que recibe la altura del árbol (un entero positivo entre 1 y 100) y un carácter especial para decorarlo.

La función debe devolver un string que represente el árbol de Navidad, construido de la siguiente manera:

El árbol está compuesto de triángulos de caracteres especiales.
Los espacios en blanco a los lados del árbol se representan con guiones bajos _.
Todos los árboles tienen un tronco de dos líneas, representado por el carácter #.
El árbol siempre debe tener la misma longitud por cada lado.
Debes asegurarte de que el árbol tenga la forma correcta usando saltos de línea \n para cada línea.
Ejemplos:

const tree = createXmasTree(5, '*')
console.log(tree)
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/

const tree2 = createXmasTree(3, '+')
console.log(tree2)
/*
__+__
_+++_
+++++
__#__
__#__
*/

const tree3 = createXmasTree(6, '@')
console.log(tree3)
/*
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
*/"""

def solution(altura:int, adorno:str) -> str:
    tronco = altura
    result = '\n'
    ancho = 1
    for i in range(1, altura + 1):
        result += '_' * (altura - 1)
        result += adorno * ancho
        result += '_' * (altura - 1)
        altura -= 1
        ancho += 2
        result += '\n'
    
    for _ in range(2):
        result += '_' * (tronco - 1)
        result += '#'
        result += '_' * (tronco - 1)
        if _ == 1:
            continue
        else:
            result += '\n'
        
    
    return result



if __name__ == '__main__':
    tree = solution(30, '*')
    print(tree)
# /*
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____
# */






