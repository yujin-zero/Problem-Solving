def solution(clothes):
    answer = 1
    clo = dict()
    
    for name, type in clothes :
        if type in clo :
            clo[type] += 1
        else :
            clo[type] = 1
    
    for t in clo.keys() :
        answer *= (clo[t] + 1)
    
    return answer - 1