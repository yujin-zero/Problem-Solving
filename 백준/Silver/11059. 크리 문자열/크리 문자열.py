import sys

s = list(sys.stdin.readline().rstrip())
n = len(s)
for i in range(n):
    s[i] = int(s[i])

if n % 2 == 0 :
    section = n
else :
    section = n-1

while True :
    for i in range(n-section + 1) :
        tmp = section//2
        f = sum(s[i:i+tmp])
        b = sum(s[i+tmp : i+tmp*2])
        if f == b :
            print(section)
            sys.exit(0)
    section -= 2