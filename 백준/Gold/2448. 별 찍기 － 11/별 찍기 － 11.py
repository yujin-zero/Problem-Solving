import sys

def star(size,row,col) :
    if size == 3 :
        graph[row][col] = '*'
        graph[row+1][col-1] = '*'
        graph[row+1][col+1] = '*'
        for i in range(5) :
            graph[row+2][col-2+i] = '*'
    else :
        size //= 2
        star(size,row,col)
        star(size,row+size,col-size)
        star(size,row+size,col+size)


n = int(sys.stdin.readline())
graph = [[' ' for _ in range(n*2)] for _ in range(n)]

star(n,0,n-1)

for g in graph :
    print("".join(g))