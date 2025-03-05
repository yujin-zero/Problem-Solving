def solution(k, m, score):
    answer = 0
    
    score.sort(reverse = True)
    i = m-1
    
    while i < len(score) :
        answer += score[i]
        i += m
    
    answer *= m
    return answer