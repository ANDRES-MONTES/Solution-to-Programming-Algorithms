def solution(upSpeed, downSpeed, desiredHeight):
    days = 0
    altura = 0
    
    while altura < desiredHeight:
        altura += upSpeed
        days += 1
        print(altura, days)

        if altura >= desiredHeight:
            break
        
        altura -= downSpeed

       
    
    return days


solution(10, 9, 4)