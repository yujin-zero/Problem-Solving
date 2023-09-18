import sys

n = sys.stdin.readline().rstrip()
while n != "":
    n = int(n)
    i = 1
    while i % n != 0:
        i = i*10 + 1
    print(len(str(i)))

    n = sys.stdin.readline().rstrip()
