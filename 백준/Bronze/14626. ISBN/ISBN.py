import sys

x = list(sys.stdin.readline().rstrip())
hap = 0
tmp = -1
answer = -1
for i in range(len(x)):
    value = x[i]
    if value == '*':
        if i % 2 == 0:
            tmp = 1
        else:
            tmp = 3
        continue
    if i % 2 == 0:
        hap += int(value)
    else:
        hap += int(value) * 3

for i in range(10):
    if (hap + tmp * i) % 10 == 0:
        answer = i
        break

print(answer)
