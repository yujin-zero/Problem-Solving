import sys

n, m = map(int,sys.stdin.readline().split())
waiting = list(map(int,sys.stdin.readline().split()))
friend = list(map(int,sys.stdin.readline().split()))
cnt = 0

for i in range(len(friend)) :
    if waiting[i] not in friend :
        cnt += 1

print(cnt)