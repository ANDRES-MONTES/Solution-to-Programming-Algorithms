"""
Ya ha entregado Santa Claus 🎅 todos los regalos a los niños pero quieren revisar si pueden mejorar de cara al año que viene.

Los elfos quieren saber cuántos movimientos ha hecho Santa Claus 🛷 para entregar todos los regalos. Para ello, te dan un mapa de la ciudad con la ubicación de cada niño y de Santa.

El mapa es una cadena de texto multi línea donde cada caracter representa una casilla. Los niños se representan por números del 1 al 9 y Santa Claus por la letra S. El resto de casillas son .

Santa Claus sólo puede moverse hacia arriba, abajo, izquierda o derecha, y cada movimiento cuenta como 1 km. Además, siempre empieza en la posición S y debe entregar los regalos en orden, del 1 al 9.

const map =
.....1....
..S.......
..........
....3.....
......2...`

const result = travelDistance(map)
console.log(result) // -> 12 km
/*
De la S al niño 1: 4 movimientos
Del niño 1 al 2: 5 movimientos
Del niño 2 al 3: 3 movimientos
Total: 12 movimientos
*/

const result2 = travelDistance(`..S.1...`)
console.log(result2) // -> 2
Escribe una función travelDistance que reciba un mapa y devuelva la distancia total que ha recorrido Santa Claus según la posición de los niños.

Ten en cuenta que:

El mapa no tiene por qué ser cuadrado.
El mapa siempre tendrá al menos un niño.
El mapa siempre tendrá una posición inicial para Santa Claus.
Los números de los niños nunca se repiten. 
"""

def distancia(mapa:str):
    data = [x for x in mapa]
    row = []
    matriz = []
    x, y = 0, 0
    distancia = 0
    
    for i in range(len(data)):
        if data[i] == "\n":
            matriz.append(row[:])
            del row[:]
        else:
            row.append(data[i])
            
            
    for i in range(len(matriz)):
        encontrado = False
        for j in range(len(matriz[i])):
            if matriz[i][j] == 'S':
                y = i
                x = j
                encontrado = True
                break
        if encontrado:
            break
            
    find_niños = [int(j) for i in range(len(matriz)) for j in matriz[i] if j in '123456789']
    find_niños.sort()
    find_niños = [str(x) for x in find_niños]
    
    coordenadas_niños = []
    coordenadas_niños.append((x, y))
    
    for i in range(len(find_niños)):
        
        for j in range(len(matriz)):
            for k in range(len(matriz[j])):
                if find_niños[i] == matriz[j][k]:
                    coordenadas_niños.append((k, j))
    
    for i in range(len(coordenadas_niños) - 1):
        x_axis = abs(coordenadas_niños[i][0] - coordenadas_niños[i + 1][0])
        y_axis = abs(coordenadas_niños[i][1] - coordenadas_niños[i + 1][1])
        distancia += x_axis + y_axis


    for i in matriz:
        print(i)
        
    print(x, y)
    print(find_niños)
    print(coordenadas_niños)
    
    
    return distancia
        
    

if __name__ == '__main__':
    map =  """.....1....
..S.......
..........
....3.....
......2...
"""



                
    result = distancia(map)
    print(result)