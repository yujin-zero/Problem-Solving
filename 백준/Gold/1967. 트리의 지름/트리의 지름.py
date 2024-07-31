import sys

n = int(sys.stdin.readline())
node = [[] for _ in range(n+1)]
childsWeight = [[] for _ in range(n+1)]
queue = []
queue2 = []
answer = 0
parent = [[] for _ in range(n+1)]
for _ in range(n-1) :
    pp, child, weight = map(int,sys.stdin.readline().split())
    node[pp].append(child)
    parent[child].append((pp,weight))

queue.append(1) 

while queue :
    currentNode = queue.pop()
    queue2.append(currentNode)
    for c in node[currentNode] :
        queue.append(c)

while queue2:
    x = queue2.pop()
    if x == 1 :
        break

    if childsWeight[x] :
        hap = max(childsWeight[x])
    else :
        hap = 0
    p,w = parent[x][0]
    childsWeight[p].append(hap+w)

for i in range(1,n+1) :
    if len(childsWeight[i]) > 2 :
        childsWeight[i].sort(reverse=True)
        tmp = childsWeight[i][0] + childsWeight[i][1]
    else :
        tmp = sum(childsWeight[i])
    if tmp > answer :
        answer = tmp

print(answer)