from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue :
        current = queue.popleft()
        cnt = 0
        
        tmp = False
        for next in queue :
            cnt += 1
            if current > next :
                answer.append(cnt)
                tmp = True
                break
                
        if not tmp :
            answer.append(cnt)
    
    return answer