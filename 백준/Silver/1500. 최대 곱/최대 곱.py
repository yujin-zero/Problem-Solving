import sys

s, k = map(int, sys.stdin.readline().split())
x = s//k
cnt = k-s+(s//k)*k
answer = 1
for _ in range(cnt):
    answer *= x
cnt = s-(s//k)*k
x += 1
for _ in range(cnt):
    answer *= x
print(answer)
