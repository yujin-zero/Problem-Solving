import sys

t = int(sys.stdin.readline())
case = []
for _ in range(t):
    case.append(int(sys.stdin.readline()))

m = max(case)
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, m+1):
    x = p[i-2] + p[i-3]
    p.append(x)

for c in case:
    print(p[c])
