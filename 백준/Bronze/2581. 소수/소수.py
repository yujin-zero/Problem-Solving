import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum = 0
min = 0
for i in range(m, n+1):
    temp = 0
    if i == 1:
        temp = 1
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            temp = 1
            break
    if temp == 0:
        sum += i
        if min == 0:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
