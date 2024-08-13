import sys

def f(i,j,cnt) :
    global answer

    if cnt > answer :
        answer = cnt

    for x, y in move :
        nextI = i + x
        nextJ = j + y
        if 0 <= nextI < r and 0 <= nextJ < c :
            nextAplha = graph[nextI][nextJ]
            if not find[ord(nextAplha)-ord('A')] :
                find[ord(nextAplha)-ord('A')] = True
                f(nextI,nextJ,cnt+1)
                find[ord(nextAplha)-ord('A')] = False

r, c = map(int,sys.stdin.readline().split())
graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(r) :
    x = list(sys.stdin.readline().rstrip())
    graph.append(x)

answer = 0
find = [False] * 26
find[ord(graph[0][0])-ord('A')] = True
f(0,0,1)
print(answer)