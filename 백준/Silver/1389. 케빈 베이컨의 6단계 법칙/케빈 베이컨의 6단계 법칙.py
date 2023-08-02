import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
people = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b not in people[a]:
        people[a].append(b)
        people[b].append(a)

kevinNum = n**2
kevinPerson = 0

for i in range(1, n+1):
    # 케빈 베이컨 구하기
    queue = deque([i])
    visit = deque([i])
    kevin = {}
    kevin[i] = 0
    while queue:
        temp = queue.popleft()
        for p in people[temp]:
            if p not in visit:
                visit.append(p)
                queue.append(p)
                kevin[p] = kevin[temp] + 1

    s = sum(kevin.values())
    if kevinNum > s:
        kevinNum = s
        kevinPerson = i

print(kevinPerson)
