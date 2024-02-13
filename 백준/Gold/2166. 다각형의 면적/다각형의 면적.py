import sys

n = int(sys.stdin.readline())
x = []
y = []
answer = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

for i in range(n):
    answer += (x[i]+x[i+1])*(y[i]-y[i+1])
print(abs(answer)/2)
