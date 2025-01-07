"""
En el taller de Santa, un elfo travieso ha estado jugando en la cadena de fabricación de regalos, añadiendo o eliminando un paso no planificado.

Tienes la secuencia original de pasos en la fabricación original y la secuencia modificada modified que puede incluir un paso extra o faltar un paso.

Tu tarea es escribir una función que identifique y devuelva el primer paso extra que se ha añadido o eliminado en la cadena de fabricación. Si no hay ninguna diferencia entre las secuencias, devuelve una cadena vacía.

const original = 'abcd'
const modified = 'abcde'
findNaughtyStep(original, modified) // 'e'

const original = 'stepfor'
const modified = 'stepor'
findNaughtyStep(original, modified) // 'f'

const original = 'abcde'
const modified = 'abcde'
findNaughtyStep(original, modified) // ''
A tener en cuenta:

Siempre habrá un paso de diferencia o ninguno.
La modificación puede ocurrir en cualquier lugar de la cadena.
La secuencia original puede estar vacía
"""

def find_step(original:str, modified:str):
    stp:str =''
    if len(original) == len(modified):
        for i in range(len(modified)):
            if original[i] == modified[i]:
                continue
            elif original[i] != modified[i]:
                stp+= modified[i]
                break
    elif len(original) > len(modified):
        try:
            for i in range(len(original)):
                if original[i] == modificado[i]:
                    continue
                elif original[i] != modificado[i]:
                    stp += original[i]
                    break
        except:
            stp += origial[i]
    
    elif len(origial) < len(modificado):
        try:
            for i in range(len(modificado)):
                if original[i] == modificado[i]:
                    continue
                elif original[i] != modificado[i]:
                    stp += modificado[i]
                    break
        except:
            stp += modificado[i]
                    
    return stp
            
            
            
if __name__ == '__main__':
    origial =    'abcd'
    modificado = 'abcde'
    
    result = find_step(origial, modificado)
    print(result)