def solution(info:str):
  #'foo((bar)lim'
  data = [x for x in info]
  i = 0
  abierto = 0
  cerrado = 0
 
   
  while i < len(data):

    if data[i] == '(':
      abierto = int(i)
      print(abierto)
      
    if data[i] == ')':
        if '(' in data:
          cerrado += i
          data[abierto: cerrado + 1] = data[abierto: cerrado + 1][::-1]
          del data[cerrado]
          del data[abierto]
          abierto = 0
          cerrado = 0
          i = 0
          continue
          
        
    i += 1
    
  
  return ''.join(data)
    
  
if __name__ == '__main__':
  data = 'foo(bar)baz(blim)'
  data_1 = 'foo(bar(ba)zb)lim'
  data_2 = 'foo(bar))lim'
  result = solution('foo((bar)lim')
  print(result)