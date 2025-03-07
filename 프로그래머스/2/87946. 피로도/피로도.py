from itertools import permutations

def solution(k, dungeons):
    answer = 0
    sunseo = [i for i in range(0,len(dungeons))]
    sunseo = list(permutations(sunseo, len(sunseo)))

    for current_sunseo in sunseo :
        tmp = k
        cnt = 0
        
        for idx in current_sunseo :
            if dungeons[idx][0] > tmp :
                break
                
            tmp -= dungeons[idx][1]
            cnt += 1
            
        answer = max(answer, cnt)
        
    return answer