import sys
from collections import deque

name = sys.stdin.readline().rstrip()
count = len(name)
pal = [0]*26

for i in range(count):
    x = ord(name[i])-65
    pal[x] += 1

alone = 0
answer = deque()

for i in range(26):
    n = pal[i]
    if n != 0:
        if n % 2 == 1:
            alone += 1
            temp = i
        for _ in range(n//2):
            answer.append(i)

if alone == 0:
    for a in answer:
        print(chr(a+65), end='')
    for i in range(len(answer)-1, -1, -1):
        print(chr(answer[i]+65), end='')
    print()
elif alone == 1:
    for a in answer:
        print(chr(a+65), end='')
    print(chr(temp+65), end='')
    for i in range(len(answer)-1, -1, -1):
        print(chr(answer[i]+65), end='')
    print()
else:
    print("I'm Sorry Hansoo")
