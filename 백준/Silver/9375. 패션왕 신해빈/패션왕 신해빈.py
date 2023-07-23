import sys

t = int(sys.stdin.readline())
answer = []

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        x = sys.stdin.readline().split()[1]
        if x not in clothes:
            clothes[x] = 1
        else:
            clothes[x] += 1
    result = 1
    for c in clothes.values():
        result *= (c+1)
    answer.append(result-1)

for a in answer:
    print(a)
