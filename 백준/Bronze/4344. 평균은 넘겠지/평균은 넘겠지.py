import sys

c = int(sys.stdin.readline())
result = []

for _ in range(c):
    score = list(map(int, sys.stdin.readline().split()))
    n = score[0]
    score = score[1: len(score)]
    hap = sum(score)
    avg = hap/n
    count = 0
    for s in score:
        if s > avg:
            count += 1
    result.append(count/n * 100)

for r in result:
    print("{:.3f}".format(r)+'%')
