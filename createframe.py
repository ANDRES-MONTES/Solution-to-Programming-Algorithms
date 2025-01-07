"""
Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es ayudar a los elfos a generar este marco mágico.

Reglas:

Dado un array de nombres, debes crear un marco rectangular que los contenga a todos.
Cada nombre debe estar en una línea, alineado a la izquierda.
El marco está construido con * y tiene un borde de una línea de ancho.
La anchura del marco se adapta automáticamente al nombre más largo más un margen de 1 espacio a cada lado.
Ejemplo de funcionamiento:

createFrame(['midu', 'madeval', 'educalvolpz'])

// Resultado esperado:
***************
* midu        *
* madeval     *
* educalvolpz *
***************

createFrame(['midu'])

// Resultado esperado:
********
* midu *
********

createFrame(['a', 'bb', 'ccc'])

// Resultado esperado:
*******
* a   *
* bb  *
* ccc *
*******

createFrame(['a', 'bb', 'ccc', 'dddd'])s
"""

def solution(names:list) -> str:
    ancho = len(max(names, key=lambda x:len(x))) + 4
    result = '*' * ancho + '\n'
    for i in range(len(names)):
        margen = ancho - len(f'* {names[i]}') - 1
        result += f"* {names[i]}{' '*margen}*"
        result += '\n'
    result += '*' * ancho
    return result
        
            
if __name__ == '__main__':
    names = ['midu', 'madeval', 'educalvolpz']
    result = solution(['a', 'bb', 'ccc', 'dddd'])
    print(result)
