"""
Los elfos están recibiendo mensajes binarios extraños desde Marte 🪐. ¿Los extraterrestres están tratando de comunicarse con ellos? 👽

El mensaje que llega es un array de 0s y 1s. Parece que han encontrado un patrón… Para asegurarse, quieren encontrar el segmento más largo de la cadena donde el número de 0s y 1s sea igual.

findBalancedSegment([1, 1, 0, 1, 1, 0, 1, 1])
//                         |________|
// posición del segmento:    [2, 5]
// más largo equilibrado
// de 0s y 1s

findBalancedSegment([1, 1, 0])
//                      |__|
//                     [1, 2]

findBalancedSegment([1, 1, 1])
// no hay segmentos equilibrados: []
Ten en cuenta que si hay más de un patrón equilibrado, debes devolver el más largo y el primero que encuentres de izquierda a derecha.

Dicen que si encuentran el patrón, podrán enviar un mensaje de vuelta a Marte 🚀. Parece ser que tienen que enviarlos a https://mars.codes.

"""


def segmento(message:list):
    unos = 0
    ceros = 0
    for i in range(len(message)):
        if message[i] == 0:
            ceros += 1
        else:
            unos += 1
            
    
    if unos == 0 or ceros == 0:
        return []
    
    valor_min = min(unos, ceros)
    len_result = valor_min * 2
    
    i = 0
    while i < len(message):
        prev = message[i:i + len_result]
        print(prev)
        print('conteo 1 =>', prev.count(1))
        print('conteo 2 =>', prev.count(0))

        if prev.count(1) == prev.count(0):
            return  [i, i + len_result - 1]
             
        else:
            i += 1
            
            
    return []



if __name__ == '__main__':
    data = [1, 1, 0, 1, 1, 0, 1, 1]
    result = segmento(data)
    print(result)