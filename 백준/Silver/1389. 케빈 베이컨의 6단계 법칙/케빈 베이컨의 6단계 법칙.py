import sys
from collections import deque


def bfs(v):
    global cnt, mn, ans
    q = deque()
    q.append(v)
    visited = [0]*101  # 몇번만에 해당 노드로 도착하는지 계산
    visited[v] = 1  # 자기 노드는 처음부터 도착하므로 1
    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                # 이전에 노드까지 가는데 걸리는 시간 + 현재 노드까지 한칸더 이동
                visited[i] = visited[t] + 1
    cnt = sum(visited)  # v가 모든 노드를 가는데 걸리는 횟수
    if mn > cnt:  # 만약 mn 보다 cnt 가 작으면
        mn = cnt  # mn은 cnt가 되고
        ans = v  # 답은 시작한 노드


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

lst = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # graph 인접리스트만들기
    graph[b].append(a)
    lst.append(a)  # 어떤 번호가 있는지 알기위해 lst에 집어넣기
    lst.append(b)

mn = 1e9
cnt = 0
ans = 0
for j in set(lst):  # lst에 있는 값으로 bfs진행
    bfs(j)

print(ans)
