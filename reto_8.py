"""
Los elfos están muy ocupados en el taller de Santa Claus organizando regalos 🎁 para la víspera de Navidad 🎄.

El formato de entrada es especial, ya que indica el número de regalos y el tipo de regalo con letras de la a a la z. Por ejemplo, '66a11b' significa 66 regalos a y 11 regalos b.

Los elfos tienen un sistema especial para organizar los regalos:

Cada 10 regalos del mismo tipo se empaquetan en una caja, representada por {x}. Por ejemplo, 20 regalos tipo a se empaquetan en 2 cajas así: {a}{a}.
Cada 5 cajas se apilan en un palé, representado por [x]. Por ejemplo, 10 cajas de a se apilan en 2 palés de esta manera: [a][a]
Cualquier regalo adicional se coloca en una bolsa, representada por () y se colocan todas dentro. Por ejemplo 4 regalos de b se colocan en una bolsa así (bbbb)
Los regalos luego se colocan en el siguiente orden: palés, cajas y bolsas. Y los regalos aparecen en el mismo orden que la cadena de entrada.

Tu tarea es escribir una función organizeGifts que tome una cadena de regalos como argumento y devuelva una cadena representando el almacén.

const result1 = organizeGifts(`76a11b`)
console.log(result1)
// '[a]{a}{a}(aaaaaa){b}(b)'

/* Explicación:

  76a: 76 regalos tipo 'a' se empaquetarían en 7 cajas y sobrarían 6 regalos, resultando en 1 palé [a] (por las primeras 5 cajas), 2 cajas sueltas {a}{a} y una bolsa con 6 regalos (aaaaaa)

  11b: 11 regalos tipo 'b' se empaquetarían en 1 caj
"""


def organize_gifts(gifts:str):
    result = ''
    num = ''
    data = {}
    for i in range(len(gifts)):
        if gifts[i].isdigit():
            num += gifts[i]

        elif gifts[i].isalpha():
            data[gifts[i]] = num
            num = ''
            
    for i in data.items():
        letra, num = i
        num = int(num)
        
        caja = 0
        pale = 0
        regalo = 0
        
        for j in range(1, num + 1):
            if j % 10 == 0:
                caja += 1
                continue
        
        regalo = num - (caja * 10)
        
        for c in range(1, caja + 1):
            if c % 5 == 0:
                pale += 1
                
        caja = caja - (pale * 5)
        
        
        for _ in range(pale):
             result += f'[{letra}]'
    
        for _ in range(caja):
            result += f'{{{letra}}}'
        
        if regalo != 0:
            bolsa = '('
            for _ in range(regalo):
                bolsa += f'{letra}'
            
            bolsa += ')'
            result += bolsa
            
            
    return result


if __name__ == '__main__':
    regalos = '76a11b'
    result = organize_gifts(regalos)
    print(result)
    