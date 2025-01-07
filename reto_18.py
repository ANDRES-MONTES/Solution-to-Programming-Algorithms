"""
En la fábrica de juguetes, los elfos están programando un reloj digital para mantenerse en horario con la producción de regalos. Sin embargo, se han encontrado con un desafío de programación interesante. Necesitan una función que, dada una hora en formato 'HH:MM', cree una representación visual de esta hora en un reloj digital devolviendo un array de arrays de caracteres.

La pantalla del reloj tiene 7 filas y 17 columnas, y cada dígito de la hora ocupa 7 filas y 3 columnas. Los dígitos están compuestos por asteriscos (*) y espacios en blanco (). Entre cada dígito hay una columna vacía.

Los dos puntos para separar horas y minutos se dibujan usando dos asteríscos (*) y siempre se colocan en la misma posición, en las filas 2 y 4, en la columna 9, respectivamente (nota: la indexación de filas y columnas comienza en 0).

Por ejemplo, si la función recibe 01:30 debe devolver:

drawClock('01:30') // ⬇️

[
  ['*', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*'],
  ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', '*'],
  ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', '*'],
  ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', '*', ' ', '*'],
  ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', '*', ' ', '*'],
  ['*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', '*'],
  ['*', '*', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', '*', '*', '*']
]
Para saber cómo dibujar cada dígito, nos han pasado la siguiente imagen. Como ves, cada dígito está compuesto por 7 filas y 3 columnas. Los píxeles en rojo, nosotros lo representaremos con un asterisco (*), y los píxeles en blanco, con un espacio ():

Representación de los dígitos para el reloj digital del 1 al 9, donde puedes ver lo que ocupa en píxeles cada número
    
"""



def draw_clock(time:str):
    result = [[' '] * 17 for _ in range(7)]
    
    for i in range(len(result)):
      for j in range(len(result[i])):
        if i == 2 or i == 4:
          if  j == 8:
            result[i][j] = '|'
            
            
    structure = time.split(':')
    info = []
    for i in range(len(structure)):
      info.append([int(x) for x in structure[i]])
    
    hora = [x for j in info for x in j]
          
    x = 0
    for i in range(len(hora)):
      
      if hora[i] == 0:
        for j in range(len(result)):
          for k in range(x, (x + 3)):
            if j == 0 or j == len(result) - 1:
              result[j][k] = '|'
            else:
              if k == x or k == x + 2:
                result[j][k] = '|'
                      
        if i == 1:
          x += 6
        else:
          x += 4
        
  
      if hora[i] == 1:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if k == x + 2:
              result[j][k] = '|'
        
        if i == 1:
          x += 6
        else:
          x += 4
        

      if hora[i] == 2:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j == 0 or j == 3 or j == len(result) - 1:
              result[j][k] = '|'
            
            elif j == 1 or j == 2:
              if k == x + 2:
                result[j][k] = '|'
                
            elif j == 4 or j == 5:
              if k == x:
                result[j][k] = '|'
        
        if i == 1:
          x += 6
        else:
          x += 4
      
      if hora[i] == 3:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j == 0 or j == 3 or j == len(result) - 1:
              result[j][k] = '|'
          
            else:
              if k == x + 2:
                result[j][k] = '|'

        if i == 1:
          x += 6
        else:
          x += 4
      
      
      if hora[i] == 4:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j < 3:
              if k == x or k == x +2:
                result[j][k] = '|'
            if j == 3:
              result[j][k] = '|'
            
            else:
              if k == x + 2:
                result[j][k] = '|'
              
        if i == 1:
          x += 6
        else:
          x += 4


      if hora[i] == 5:
        for j in range(len(result)):
          for k in range(x + x + 3):
            if j == 0 or j == 3 or j == len(result) - 1:
              result[j][k] = '|'
            elif j > 0 and j < 3:
              if k == x:
                result[j][k] = '|'
            else:
              if k == x + 2:
                result[j][k] = '|'
            
        if i == 1:
          x += 6
        else:
          x += 4
      
      if hora[i] == 6:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j == 0 or j == 3 or j == len(result) -1:
              result[j][k] = '|'
            elif j > 0 and j < 3:
              if k == x:
                result[j][k] = '|'
            elif j > 3:
              if k == x or k == x + 2:
                result[j][k] = '|'
        
        if i == 1:
          x += 6
        else:
          x += 4
      
      if hora[i] == 7:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j == 0:
              result[j][k] = '|'
              
            elif j == 3:
              if k >= x + 1:
                result[j][k] = '|'
              
            else:
              if k == x + 2:
                result[j][k] = '|'
        
        
        if i == 1:
          x += 6
        else:
          x += 4

      if hora[i] == 8:
        for j in range(len(result)):
          for k in range(x + x + 3):
            if j == 0 or j == 3 or j == len(result) - 1:
              result[j][k] = '|'
            
            else:
              if k == x or k == x + 2:
                result[j][k] = '|'
        
        if i == 1:
          x += 6
        else:
          x += 4

      if hora[i] == 9:
        for j in range(len(result)):
          for k in range(x, x + 3):
            if j == 0 or j == 3 or j == len(result) - 1:
              result[j][k] = '|'
            elif j > 0 and j < 3:
              if k == x or k == x + 2:
                result[j][k] = '|'
              
            else:
              if k == x + 2:
                result[j][k] = '|'
        
      
        if i == 1:
          x += 6
        else:
          x += 4
    
    
    return result


if __name__ == '__main__':
    hora = '24:24'
    result = draw_clock(hora)
    for i in result:
      print(i)
    