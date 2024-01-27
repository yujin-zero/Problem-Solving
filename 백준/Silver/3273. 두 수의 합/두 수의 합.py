import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
answer = 0
num = dict()
for l in lst:
    if l in num:
        num[l] += 1
    else:
        num[l] = 1
for i in num:
    j = x-i
    if j in num:
        answer += num[i]*num[j]
answer //= 2
print(answer)
