import sys

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
a = round(n*(15/100)+0.000001)
b = n-a
level = 0
k = []
for i in range(n):
    x = int(sys.stdin.readline())
    k.append(x)
k.sort()


for i in range(a, b):
    level += k[i]

level /= (b - a)
print(round(level+0.000001))
