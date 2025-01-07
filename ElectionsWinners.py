def solution(votes, k):
    if k == 0: 
        maximo = max(votes)
        if votes.count(maximo) == 1:
            return  1
        else:
            return 0
        
    sumados = map(lambda x : x + k, votes)
    alto = max(votes)
    filtrados = filter(lambda x : x > alto, sumados)
    
    return len(list(filtrados))


        
if __name__ == '__main__':
    votes, k=  [2, 3, 5, 2], 0
    
    result = solution(votes, k)
    print(result)
