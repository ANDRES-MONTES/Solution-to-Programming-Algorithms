"""

Los elfos están preparando la víspera de Navidad y necesitan tu ayuda para calcular si van sobrados o no de tiempo ⏳.

Para ello te pasan un array con la duración de cada entrega. El formato de la duración es HH:mm:ss, las entregas empiezan a las 00:00:00 y el límite de tiempo es 07:00:00.

Tu función debe devolver el tiempo que les faltará o el tiempo que les sobrará para terminar las entregas. El formato de la duración devuelta debe ser HH:mm:ss.

Si terminan antes de las 07:00:00, el tiempo restante hasta las 07:00:00 debe ser mostrado con un signo negativo. Por ejemplo, si sobran 1 hora y 30 minutos, devuelve -01:30:00

calculateTime(['00:10:00', '01:00:00', '03:30:00'])
// '-02:20:00'

calculateTime(['02:00:00', '05:00:00', '00:30:00'])
// '00:30:00'

calculateTime([
  '00:45:00',
  '00:45:00',
  '00:00:30',
  '00:00:30'
]) // '-05:29:00'
    
"""



def calculate_time(deliveries:list):
    result = ''
    limite = 420     #limite de horas en minutos
    store = [0, 0, 0]
    info = []
    
    for i in range(len(deliveries)):
        separate = deliveries[i].split(':')
        data = [int(x) for x in separate]
        info.append(data)
        
        
    for i in range(len(info)):
        for j in range(len(info[i])):
            store[j] += info[i][j]
            
    hora, min, seg = store

    
    for i in range(1, seg + 1):
        if i % 60 == 0:
            min += 1
            seg -= 60
            
    for i in range(1, min + 1):
        if i % 60 == 0:
            hora += 1
            min -= 60
            
            
    store = [hora, min, seg]
    total_minutes = (store[0] * 60) + store[1]
    
    tiempo = limite - total_minutes
    hora = 0
        
    for i in range(1, tiempo + 1):
        if i % 60 == 0:
            hora += 1
            tiempo -= 60
            
        

    hora_final = [hora, tiempo, store[2]]
    
    to_string = [str(x) for x in hora_final]
    
    for i in range(len(to_string)):
        if len(to_string[i]) == 1:
            to_string[i] = f'0{to_string[i]}'
        
    
    data = ':'.join(to_string)
    
    for i in range(len(data)):
        if data[i] != '-':
            continue
        if data[i] == '-':
            result = data.replace('-', '')
            return result
        
    result = f'-{data}'
    return result


if __name__ == '__main__':
    data = ['00:10:00', '01:00:00', '03:30:00']
    data_2 = ['02:00:00', '05:00:00', '00:30:00']
    data_3 = ['00:45:00', '00:45:00', '00:00:30', '00:00:30']
    
    result = calculate_time(data_3)
    print(result)