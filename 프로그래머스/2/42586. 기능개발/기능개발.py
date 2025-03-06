from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    
    queue = deque()
    len_progress = len(progresses)
    for i in range(len_progress) :
        left_day = math.ceil((100-progresses[i]) / speeds[i])
        queue.append(left_day)
    
    while queue :
        tmp = 1
        current_day = queue.popleft()
        
        while queue and queue[0] <= current_day :
            queue.popleft()
            tmp += 1
            
        answer.append(tmp)
        
    return answer