"""
Ya hemos empaquetado cientos de regalos 🎁… pero a un elfo se le ha olvidado revisar si el regalo, representado por un asterisco *, está dentro de la caja.

La caja tiene un regalo (*) y cuenta como dentro de la caja si:

Está rodeada por # en los bordes de la caja.
El * no está en los bordes de la caja.
Ten en cuenta entonces que el * puede estar dentro, fuera o incluso no estar. Y debemos devolver true si el * está dentro de la caja y false en caso contrario.

Ejemplos:

inBox([
  "###",
  "#*#",
  "###"
]) // ➞ true

inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]) // ➞ true

inBox([
  "#####",
  "#   #",
  "#  #*",
  "#####"
]) // ➞ false

inBox([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) // ➞ false    
"""


def solution(box:list[str]) -> bool:
    box = [[j for j in i] for i in box]
    
    regalo=None
    for i in range(len(box)):
        for j in range(len(box[i])):
            if box[i][j] == '*':
                regalo = (j, i)
                break
        if regalo:
          break
      
    
    if regalo:
        if box[regalo[1]][0] == '#' and box[regalo[1]][-1] == '#' and box[0][regalo[0]] == '#' and box[-1][regalo[0]] == '#':
          return True
        else:
          return False
    else:
        return False
      
        

            
    
    

if __name__ == '__main__':
    data =[
        "####",
        "#* #",
        "#  #",
        "####"
        ]
    result = solution(data)
    print(result)