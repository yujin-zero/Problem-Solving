import sys

n = int(sys.stdin.readline())
if n == 1 :
     print(0)
     sys.exit(0)
sosu = []
isSosu = [True] * (n+1)
start, end = 0, 0
cnt = 0
for i in range(2,n+1) :
    if isSosu[i] :
        sosu.append(i)
        for j in range(2*i, n+1, i) :
                isSosu[j] = False
hap = sosu[0]
lenSosu = len(sosu)

while True :
    if hap <= n :
        if hap == n :
            cnt += 1
        end += 1
        if end == lenSosu :
            break
        hap += sosu[end]
    else :
        hap -= sosu[start]
        start += 1


print(cnt)