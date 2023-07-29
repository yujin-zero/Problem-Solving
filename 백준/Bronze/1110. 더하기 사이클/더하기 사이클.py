import sys

n = int(sys.stdin.readline())

start = n
if n < 10:
    x = 0
    y = n
else:
    x = int(str(n)[0])
    y = int(str(n)[1])
sum = x+y
n = int(str(sum)[-1]) + y*10
cycle = 1
while n != start:
    if n < 10:
        x = 0
        y = n
    else:
        x = int(str(n)[0])
        y = int(str(n)[1])
    sum = x+y
    n = int(str(sum)[-1]) + y*10
    cycle += 1

print(cycle)
