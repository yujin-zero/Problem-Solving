import sys
sys.setrecursionlimit(10**6)

def DFS(currentStu) :
    global cnt
    visit[currentStu] = True
    tmp.append(currentStu)
    nextStu = choice[currentStu] - 1

    if visit[nextStu] :
        if nextStu in tmp :
            cnt += len(tmp[tmp.index(nextStu):])
    else :
        DFS(nextStu)


t = int(sys.stdin.readline())
for _ in range(t) :
    n = int(sys.stdin.readline()) 
    choice = list(map(int,sys.stdin.readline().split()))
    visit = [False] * n
    cnt = 0

    for i in range(n) :
        if not visit[i] :
            tmp = []
            DFS(i)

    print(n-cnt)