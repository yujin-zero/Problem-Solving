import sys
sys.setrecursionlimit(10**6)

def DFS(currentNode) :
    visit[currentNode] = True 

    for nextNode in graph[currentNode] :
        if not visit[nextNode] :
            answer[currentNode] += DFS(nextNode)
    
    return answer[currentNode]


n, r, q = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
answer = [1] * (n+1)
for _ in range(n-1) : 
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

DFS(r)

for _ in range(q) :
    x = int(sys.stdin.readline())
    print(answer[x])
