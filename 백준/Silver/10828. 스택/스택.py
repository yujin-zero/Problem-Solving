import sys

n = int(sys.stdin.readline())
s = []

for _ in range(n):
    oper = sys.stdin.readline()

    if "push" in oper:
        x = int(oper.split()[1])
        s.append(x)
    elif "pop" in oper:
        if s == []:
            print(-1)
        else:
            print(s.pop())
    elif "size" in oper:
        print(len(s))
    elif "empty" in oper:
        if s == []:
            print(1)
        else:
            print(0)
    elif "top" in oper:
        if s == []:
            print(-1)
        else:
            print(s[-1])
