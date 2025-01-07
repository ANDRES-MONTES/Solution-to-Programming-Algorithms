"""
¡Es hora de seleccionar a los renos más rápidos para los viajes de Santa! 🦌🎄
Santa Claus ha organizado unas emocionantes carreras de renos para decidir cuáles están en mejor forma.

Tu tarea es mostrar el progreso de cada reno en una pista de nieve en formato isométrico.

La información que recibes:

indices: Un array de enteros que representan el progreso de cada reno en la pista:
0: El carril está vacío.
Número positivo: La posición actual del reno desde el inicio de la pista.
Número negativo: La posición actual del reno desde el final de la pista.
length: La longitud de cada carril.
Devuelve un string que represente la pista de la carrera:

Cada carril tiene exactamente length posiciones llenas de nieve (~).
Cada reno se representa con la letra r.
Los carriles están numerados al final con /1, /2, etc.
La vista es isométrica, por lo que los carriles inferiores están desplazados hacia la derecha.
Ejemplos:

drawRace([0, 5, -3], 10)
/*
  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3
*/

drawRace([2, -1, 0, 5], 8)
/*
   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4
*/

drawRace([3, 7, -2], 12)
/*
  ~~~r~~~~~~~~ /1
 ~~~~~~~r~~~~ /2
~~~~~~~~~~r~ /3
*/
"""

def solution(indices:list[int], length:int) -> str:
    result = '\n'
    espacio = len(indices) - 1
    conteo = 1
    for i in range(len(indices)):
        result += ' '* espacio
        linea = list('~' * length)
        
        if indices[i] == 0:
            result += ''.join(linea)
        else:
            if indices[i] < 0:
                indice = (length + indices[i])
                linea[indice] = 'r'
                result += ''.join(linea)
                
            else:
                linea[indices[i]] = 'r'
                result += ''.join(linea)
                
        result += f' /{conteo}'
        conteo += 1
        espacio -=1
        
        if i == len(indices) -1 :
            break
        else:
            result += '\n'
        
        
    return result
        
        
if __name__ == '__main__':
    result = solution([3, 7, -2], 12)
    print(result)
