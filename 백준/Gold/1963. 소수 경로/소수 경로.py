import sys
from collections import deque

sosu = set()
isSosu = [True] * 10000
for i in range(2,10000) :
    if isSosu[i] :
        sosu.add(i)
        for j in range(i*2,10000,i) :
            isSosu[j] = False

t = int(sys.stdin.readline())
for _ in range(t) :
    a, b = map(int,sys.stdin.readline().split())
    visit = set()
    queue = deque()
    queue.append((a,0)) # 현재값, count 
    visit.add(a)

    while queue :
        x, y  = queue.popleft()
        # print(x,y)
        if x == b :
            print(y)
            break

        i = 1
        while i < 10000 :
            z = (x // i) % 10 # 현재 자릿수
            tmp1 = x - z*i
            for j in range(10) :
                tmp = tmp1 + j*i 
                if (1000 < tmp < 10000) and (tmp in sosu) and (tmp not in visit):
                    queue.append((tmp,y+1))
                    visit.add(tmp)
            i *= 10
