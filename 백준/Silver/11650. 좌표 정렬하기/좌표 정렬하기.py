import sys

n = int(sys.stdin.readline())
point = []

for _ in range(n):
    x, y = sys.stdin.readline().split()
    point.append([int(x), int(y)])

point.sort(key=lambda x: (x[0], x[1]))

for i in point:
    print(i[0], i[1])
