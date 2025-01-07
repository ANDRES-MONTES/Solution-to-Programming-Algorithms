"""
Santa está experimentando con nuevos diseños de regalos y necesita tu ayuda para visualizarlos en 3D.

Tu tarea es escribir una función que, dado un tamaño n (entero), genere un dibujo de un regalo en 3D utilizando caracteres ASCII.

Las líneas de los regalos se dibujan con # y las caras con el símbolo que nos pasan como parámetro:

drawGift(4, '+')

/*
   #### 
  #++##
 #++#+#
####++#
#++#+#
#++##
####
*/

drawGift(5, '*')
/*
    #####                   ######
   #***##                  #****##
  #***#*#                 #****#*# 
 #***#**#                #****#**#
#####***#               #****#***#
#***#**#               ######****#
#***#*#                #****#***# 
#***##                 #****#**#
#####                  #****#*#
*/                     #****##
                       ######  
drawGift(1, '^')
/*
#
*/
Importante: Nos han dicho que siempre hay que dejar un salto de línea al final del dibujo.

Nota: Ten en cuenta que, en los tests, la primera línea se ve empujada por el caracter ".
    
"""


def draw_gift(size:int, symbol_str):
    result = '\n'
    lineas = size + (size - 1)
    espacio = (size - 1)
    
    for i in range(1, lineas + 1):
        if i == 1:
            result += ' ' * espacio
            result += '#' * size
            espacio -= 1
            result += '\n'
            
        if i > 1 and i < size:
            result += ' ' * espacio
            final = (size + (size - 1)) - espacio
            
            for j in range(1, ((size + (size - 1)) - espacio) + 1):
                if j == 1 or j == size or j == final:
                    result += '#'
                else:
                    result += symbol_str
                    
            result += '\n'
            espacio -= 1
                 
                 
        if i == size:
            final = size + (size - 1) 
            for j in range(1, (size + (size - 1)) + 1):
                if j <= size or j == final:
                    result += '#'
                else:
                    result += symbol_str
            espacio += 1  
            result += '\n'
            
            
        if i > size and i < lineas:
            ultimo = (size + (size - 1)) - espacio
            for j in range(1, ((size + (size - 1)) - espacio) + 1):
                if j == 1 or j == size or j == ultimo:
                    result += '#'
                else:
                    result += symbol_str
            
            result += '\n'
            espacio += 1
                
            
        if i == lineas:
            result += '#' * size
            result += '\n'


    result += '\n'                
    return result


if __name__ == '__main__':
    result = draw_gift(8, '*')
    print(result)
