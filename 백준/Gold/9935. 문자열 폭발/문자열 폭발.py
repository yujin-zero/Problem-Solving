import sys

head = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
firstChar = bomb[0]
bomb.reverse()
tail = []
lenBomb = len(bomb)

while head :
    x = head.pop()

    tail.append(x)

    if x == firstChar and len(tail) >= lenBomb:
        if tail[len(tail)-lenBomb:len(tail)] == bomb :
            for _ in range(lenBomb) :
                tail.pop()

if tail :
    print("".join(reversed(tail)))
else :
    print("FRULA")