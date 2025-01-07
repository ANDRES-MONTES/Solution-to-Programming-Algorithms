"""
En el taller de Santa 🎅, algunos mensajes navideños han sido escritos de manera peculiar: las letras dentro de los paréntesis deben ser leídas al revés

Santa necesita que estos mensajes estén correctamente formateados. Tu tarea es escribir una función que tome una cadena de texto y revierta los caracteres dentro de cada par de paréntesis, eliminando los paréntesis en el mensaje final.

Eso sí, ten en cuenta que pueden existir paréntesis anidados, por lo que debes invertir los caracteres en el orden correcto.

const a = decode('hola (odnum)')
console.log(a) // hola mundo

const b = decode('(olleh) (dlrow)!')
console.log(b) // hello world!

const c = decode('sa(u(cla)atn)s')
console.log(c) // santaclaus

// Paso a paso:
// 1. Invertimos el anidado -> sa(ualcatn)s
// 2. Invertimos el que queda -> santaclaus
Notas:

Las cadenas de entrada siempre estarán bien formadas con paréntesis que coinciden correctamente, no necesitas validarlos.
En el mensaje final no deben quedar paréntesis.
El nivel máximo de anidamiento es 2.

"""


def decode(message:str):
    fixed:str = '' #(olleh) (dlrow)!
    i = 0          #sa(u(cla)atn)s
    while i < len(message):
        if message[i] == '(':
            reverd = ''
            i += 1
            while message[i] != ')':
                if message[i] == '(':
                    save = ''
                    i += 1
                    while message[i] != ')':
                        save += message[i]
                        i += 1
                    i += 1
                    save = save[::-1]
                    reverd += save
                else:
                    reverd += message[i]
                    i += 1
            i += 1
            reverd = reverd[::-1]
            fixed += reverd
          
        else:
            fixed += message[i]
            i += 1
    
    
    
    return fixed


            
    
if __name__ == '__main__':
    a = 'hola (odnum)'
    b = '(olleh) (dlrow)!'
    c = 'sere (le) (rojem)'
    d = 'sa(u(cla)atn)s'
    result = decode(d)
    print(result)