import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
# card = [*map(int, sys.stdin.readline().split())]

# 1~100000
existCard = [False]*1000001
for c in card:
    existCard[c] = True
score = [0]*1000001

for c in card:
    for i in range(c*2, 1000001, c):
        if existCard[i]:
            score[c] += 1
            score[i] -= 1

for c in card:
    print(score[c], end=' ')
