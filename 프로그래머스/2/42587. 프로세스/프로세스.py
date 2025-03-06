from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(enumerate(priorities))

    while queue :
        idx, current_process = queue.popleft()
        
        if not queue :
            answer += 1
            break

        if current_process >= max(queue, key = lambda x : x[1])[1] :
            answer += 1
            if idx == location :
                break
        else :
            queue.append((idx, current_process))
        
    return answer