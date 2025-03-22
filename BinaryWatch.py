def readBinaryWatch(turnedOn: int) -> list[str]:
    import itertools, collections
    if turnedOn > 8:
        return []
    
    horas, minutos = [8, 4, 2, 1], [32, 16, 8, 4, 2, 1]
    horas_disponibles, minutos_disponibles= collections.defaultdict(list), collections.defaultdict(list)
    
    horas_disponibles[0].append(0)
    minutos_disponibles[0].append(0)
    
    for i in range(1, len(horas) + 1):
        values = itertools.combinations(horas, i)
        for j in values:
            if sum(j) > 11:
                continue
            else:
                horas_disponibles[i].append(sum(j))
                
    for i in range(1, len(minutos) + 1):
        values = itertools.combinations(minutos, i)
        for j in values:
            if sum(j) > 59:
                continue
            else:
                minutos_disponibles[i].append(sum(j))
                
     
    print(dict(horas_disponibles))
    print(dict(minutos_disponibles))

    #empezar con el maximo de horas e ir reducionedo
    data = []
    for b_hours in range(min(turnedOn, 3) + 1):
        b_minutes = turnedOn - b_hours
        if (b_hours in horas_disponibles) and (b_minutes in minutos_disponibles):
            for i in horas_disponibles[b_hours]:
                for j in minutos_disponibles[b_minutes]:
                    data.append(f'{i}:{j:02d}')
    return data
                    
    

        
if __name__ == '__main__':
     turnedOn = 4
     result = readBinaryWatch(turnedOn)
     print(result)
