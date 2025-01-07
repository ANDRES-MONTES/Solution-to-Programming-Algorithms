"""
¡Vaya idea ha tenido Sam Elfman! Quiere ofrecer un servicio que te crea un árbol de Navidad 🎄 personalizado en cuestión de segundos.

Para crearlo nos pasan una cadena de caracteres para formar el árbol y un número que indica la altura del mismo.

Cada carácter de la cadena representa un adorno del árbol, y vamos utilizándolos de forma cíclica hasta llegar a la altura indicada. Como mínimo siempre nos pasarán uno.

Debemos devolver un string multilínea con el árbol de Navidad formado con los adornos, la altura indicada más una última línea con el tronco formado por el carácter | en el centro y, finalmente, un salto de línea \n.

Por ejemplo si recibimos la cadena "123" y el número 4 como altura, tendríamos que construir este árbol:

   1
  2 3
 1 2 3
1 2 3 1
   |
Si recibimos la cadena *@o y el número 3, el árbol que debemos devolver es:

  *
 @ o
* @ o
  |
Nota:

El árbol siempre debe estar centrado, para ello añade espacios en blanco a la izquierda de cada línea.
Crea espacios sólo a la izquierda de cada línea del árbol. No dejes espacios en blanco a la derecha.
Los adornos tienen un espacio en blanco entre ellos de separación.
Si te fallan los tests y visualmente parece que el árbol está bien, comprueba que no haya espacios en blanco que sobren, especialmente a la derecha de cada línea.

"""


def create_christmas_tree(ornaments:str, height:int):
    result = ''
    espacio = height  - 1
    ancho = 1
    adorno = 0
    for _ in range(1, height + 1):
        result += ' ' * espacio

        for j in range(ancho):      
            if j + 1  == ancho:
                result += ornaments[adorno]
                adorno += 1
                
                if adorno == len(ornaments):
                     adorno = 0
                
                continue

            result += ornaments[adorno]
            result += ' '
            adorno += 1
            
            if adorno == len(ornaments):
                adorno = 0
                
        espacio -= 1
        ancho += 1
        result += '\n'
        
    
    result += ' ' * (height - 1 )
    result += '|'
    
    
    return result


if __name__ == '__main__':
    cadena = '*@o'
    altura = 8
    result = create_christmas_tree(cadena, altura)
    print(result)