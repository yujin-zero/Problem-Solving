import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().rstrip()
    y = len(x)
    tmp = 0  # 회문임
    for i in range(y//2):
        if x[i] != x[y-1-i]:
            tmp = 1  # 회문아님
    if tmp == 0:
        print(0)  # 회문임
    else:  # 유사회문판별
        a = 0
        b = y-1
        tmp2 = 0
        cnt = 0  # 불일치횟수
        while True:
            if a >= b:
                break
            if x[a] == x[b]:
                a += 1
                b -= 1
            else:
                if cnt > 0:
                    tmp2 += 1
                    break  # 왼쪽으로 했을 땐 유사회문 아님
                a += 1
                cnt += 1
        if tmp2 == 0:
            print(1)
        else:
            a = 0
            b = y-1
            tmp2 = 0
            cnt = 0
            while True:
                if a >= b:
                    break
                if x[a] == x[b]:
                    a += 1
                    b -= 1
                else:
                    if cnt > 0:
                        tmp2 += 1
                        break
                    b -= 1
                    cnt += 1
            if tmp2 == 0:
                print(1)
            else:
                print(2)
