import sys
from collections import deque

N = int(sys.stdin.readline())
number_people = [0] + list(map(int,sys.stdin.readline().split()))
town = [[] for _ in range(N+1)]
cnt_connect = [0] * (N+1)
visit = [False] * (N+1)
dp = [[0,0] for _ in range(N+1)]
for _ in range(N-1) :
    A, B = map(int,sys.stdin.readline().split())
    town[A].append(B)
    town[B].append(A)
    cnt_connect[A] += 1
    cnt_connect[B] += 1

queue = deque()
for i in range(1,N+1) :
    if cnt_connect[i] == 1 :
        queue.append(i)
        visit[i] = True

while queue :
    current_town = queue.popleft()
    
    # 우수 마을 아닌 경우
    # 인접한 마을 중 방문한 노드들의 최댓값 찾기
    tmp = 0
    for neighbor in town[current_town] :
        if visit[neighbor] :
            tmp += max(dp[neighbor])
    dp[current_town][0] = tmp

    # 우수 마을인 경우
    # 인접한 마을 중 방문한 노드들의 우수마을 아닌 경우에서의 최댓값 찾기
    tmp = 0
    for neighbor in town[current_town] :
        if visit[neighbor] :
            tmp += dp[neighbor][0]
    dp[current_town][1] = tmp + number_people[current_town]

    # 큐에 추가
    for neighbor in town[current_town] :
        if not visit[neighbor] :
            cnt_connect[neighbor] -= 1
            if cnt_connect[neighbor] == 1 :
                queue.append(neighbor)
                visit[neighbor] = True

print(max(dp[current_town]))