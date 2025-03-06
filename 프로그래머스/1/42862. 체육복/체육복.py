def solution(n, lost, reserve):
    answer = 0
    
    clothes = [1] * (n+2)
    for l in lost :
        clothes[l] -= 1
    for r in reserve :
        clothes[r] += 1
    
    for i in range(1, n+1) :
        if clothes[i] > 0 :
            answer += 1
        else :
            if clothes[i-1] > 1 :
                clothes[i-1] -= 1
                clothes[i] += 1
                answer += 1
            elif clothes[i+1] > 1 :
                clothes[i+1] -= 1
                clothes[i] += 1
                answer += 1
    
    return answer