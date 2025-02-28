from collections import deque

def solution(n, computers):
    answer = 0
    
    queue = deque()
    visit = [False] * n
    
    for i in range(n) :
        if visit[i] :
            continue
        
        queue.append(i)
        visit[i] = True
        answer += 1
        
        while queue :
            current_computer = queue.popleft()
            
            for j in range(n) :
                if computers[current_computer][j] == 1 and not visit[j] :
                    visit[j] = True
                    queue.append(j)
            
    return answer