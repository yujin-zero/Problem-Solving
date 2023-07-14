import sys

n = int(sys.stdin.readline())

i = 0
while (n >= 3):
    if n <= 12 and n % 3 == 0:
        n -= 3
        i += 1
    elif n >= 5:
        n -= 5
        i += 1
    else:
        break

if n != 0:
    print(-1)
else:
    print(i)
