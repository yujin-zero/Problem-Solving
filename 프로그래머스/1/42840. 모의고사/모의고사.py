def solution(answers):
    answer = []
    
    score = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    len_a = len(answers)
    
    for i in range(len_a) :
        a = answers[i]
        
        if one[i%5] == a :
            score[0] += 1
        if two[i%8] == a :
            score[1] += 1
        if thr[i%10] == a :
            score[2] += 1
    
    max_s = max(score)
    for i in range(3) :
        if score[i] == max_s :
            answer.append(i+1)
    
    return answer