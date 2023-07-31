import sys

n = int(sys.stdin.readline())
count = 0
times = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append([start, end])

times.sort(key=lambda x: (x[1], x[0]))

endTime = 0
for t in times:
    if endTime <= t[0]:
        endTime = t[1]
        count += 1


print(count)
