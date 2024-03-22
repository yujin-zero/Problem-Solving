import sys


def dfs(depth):
    if depth == len(zero):
        for s in result:
            print(''.join(map(str, s)))
        exit()

    nr, nc = zero[depth]
    for i in range(1, 10):
        tmp1, tmp2, tmp3 = 1, 1, 1
        for j in range(9):
            if result[nr][j] == i:
                tmp1 = 0
                break
        for j in range(9):
            if result[j][nc] == i:
                tmp2 = 0
                break
        for j in range(3):
            for k in range(3):
                if result[(nr//3)*3+j][(nc//3)*3+k] == i:
                    tmp3 = 0
                    break

        if tmp1 == 1 and tmp2 == 1 and tmp3 == 1:
            result[nr][nc] = i
            dfs(depth+1)
            result[nr][nc] = 0


zero = []
result = []
for _ in range(9):
    result.append(list(map(int, sys.stdin.readline().strip())))

for i in range(9):
    for j in range(9):
        if result[i][j] == 0:
            zero.append((i, j))

dfs(0)
