"""
Santa 🎅 está probando su nuevo trineo eléctrico, el CyberReindeer, en una carretera del Polo Norte. La carretera se representa con una cadena de caracteres, donde:

. = Carretera
S = Trineo de Santa
* = Barrera abierta
| = Barrera cerrada
Ejemplo de carretera: S...|....|.....

Cada unidad de tiempo, el trineo avanza una posición a la derecha. Si encuentra una barrera cerrada, se detiene hasta que la barrera se abra. Si está abierta, la atraviesa directamente.

Todas las barreras empiezan cerradas, pero después de 5 unidades de tiempo, se abren todas para siempre.

Crea una función que simule el movimiento del trineo durante un tiempo dado y devuelva un array de cadenas representando el estado de la carretera en cada unidad de tiempo:

const road = 'S..|...|..'
const time = 10 // unidades de tiempo
const result = cyberReindeer(road, time)

/* -> result:
[
  'S..|...|..', // estado inicial
  '.S.|...|..', // avanza el trineo la carretera
  '..S|...|..', // avanza el trineo la carretera
  '..S|...|..', // el trineo para en la barrera
  '..S|...|..', // el trineo para en la barrera
  '...S...*..', // se abre la barrera, el trineo avanza
  '...*S..*..', // avanza el trineo la carretera
  '...*.S.*..', // avanza el trineo la carretera
  '...*..S*..', // avanza el trineo la carretera
  '...*...S..', // avanza por la barrera abierta
]
*/
El resultado es un array donde cada elemento muestra la carretera en cada unidad de tiempo.

Ten en cuenta que si el trineo está en la misma posición que una barrera, entonces toma su lugar en el array.

Los elfos se inspiraron en este reto de Code Wars.
"""
import time

def cyberReindeer(road:str, time:int):
  road_trip =  [x for x in road]
  back_up = [x for x in road]
  trineo = road_trip.index('S')
  result = [road]
  
  for i in range(2, time + 1):
    if i > 5:
      for i in range(len(road_trip)):
        if road_trip[i] == '|':
          road_trip[i] = '*'
    
    if road_trip[trineo + 1] == '.':
      road_trip[trineo], road_trip[trineo + 1] = '.', 'S'
      trineo += 1
      if back_up[trineo - 1] == '|':
        road_trip[trineo - 1] = '*'
      
    if road_trip[trineo + 1] == '*':
      road_trip[trineo], road_trip[trineo + 1] = '.', 'S'
      trineo += 1
      
      
    value = ''.join(road_trip)
    result.append(value)
    

  return result
  



   

if __name__ == '__main__':
     road = 'S..|...|..'
     road_2 = 'S.|.........|..|..........|'
     tiempo = 10# unidades de tiempo
     result = cyberReindeer(road_2, tiempo)
     for i in result:
       print(i)
       time.sleep(1)

