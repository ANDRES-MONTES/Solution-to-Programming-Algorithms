"""
¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha montado. Ha cambiado el orden de algunos paquetes, por lo que los envíos no se pueden realizar.

Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch para desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar los paquetes. Las instrucciones que siguen son:

Recibirás un string que contiene letras y paréntesis.
Cada vez que encuentres un par de paréntesis, debes voltear el contenido dentro de ellos.
Si hay paréntesis anidados, resuelve primero los más internos.
Devuelve el string resultante con los paréntesis eliminados, pero con el contenido volteado correctamente.
Nos ha dejado algunos ejemplos:

fixPackages('a(cb)de')
// ➞ "abcde"
// Volteamos "cb" dentro de los paréntesis

fixPackages('a(bc(def)g)h')
// ➞ "agdefcbh"
// 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

fixPackages('abc(def(gh)i)jk')
// ➞ "abcighfedjk"
// 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

fixPackages('a(b(c))e')
// ➞ "acbe"
// 1º volteamos "c" → "c", luego "bc" → "cb"    
    
"""

def solution(package:str) -> str:
    data = list(package)
    i = 0
    apertura = None
    cierre = None
    
    while i < len(data):
        if data[i] == '(':
            apertura = i
        
        if data[i] == ')':
            if '(' not in data:
                i += 1
            else:
                cierre = i                
                data[apertura:cierre + 1] = data[apertura + 1:cierre][::-1]
                i = 0
                apertura = 0
                cierre = 0
                
        i += 1
    
    return ''.join(data)

        
       

        
        

if __name__ == '__main__':
    info = 'abc(def(gh)i)jk'
    #"abcighfedjk"
    #"abcighfedjk"
    result = solution('(abc(def(ghi)))')
    #"defihgcba"
    #(abcdefih
    print(result)
    



