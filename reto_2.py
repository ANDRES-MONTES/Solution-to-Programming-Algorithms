"""
Los regalos son cadenas de texto y los materiales son caracteres. Tu tarea es escribir una función que, dada una lista de regalos y los materiales disponibles, devuelva una lista de los regalos que se pueden fabricar.

Un regalo se puede fabricar si contamos con todos los materiales necesarios para fabricarlo.

const gifts = ['tren', 'pelota', 'oso']
const materials = 'tronesa'

manufacture(gifts, materials) // ["tren", "oso"]
// 'tren' SÍ porque sus letras están en 'tronesa'
// 'oso' SÍ porque sus letras están en 'tronesa'
// 'pelota' NO porque sus letras NO están en 'tronesa'

const gifts = ['juego', 'puzzle']
const materials = 'jlepuz'

manufacture(gifts, materials) // ["puzzle"]

const gifts = ['libro', 'ps5']
const materials = 'psli'

manufacture(gifts, materials) // []


"""

def manufacture(gifts:list, material:str):
    fabricados = []
    for i in gifts:
        salto = False
        for j in i:
            if j not in material:
                salto = True
                break
            else:
                continue
            
        if salto:
            continue
        
        fabricados.append(i)
        
    return fabricados


if __name__ == '__main__':
    regalos =  ['tren', 'oso', 'pelota']
    material = 'tronesa'
    result = manufacture(regalos, material)
    print(result)
       
                
            
        
        
    
    
    