def solution(citations):
    answer = -1
    
    citations.sort(reverse = True)
    len_c = len(citations)
    
    if citations[0] == 0 :
        return 0
    
    for i in range(len_c) :
        cnt = i + 1
        value = citations[i]
        
        answer = max(answer, min(cnt,value))
    
    return answer