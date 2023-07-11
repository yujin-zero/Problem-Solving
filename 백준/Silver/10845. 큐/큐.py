import sys

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    oper = sys.stdin.readline()

    if "push" in oper:
        x = int(oper.split(' ')[1])
        q.append(x)
    elif "pop" in oper:
        if q == []:
            print(-1)
        else:
            print(q.pop(0))
    elif "size" in oper:
        print(len(q))
    elif "empty" in oper:
        if q == []:
            print(1)
        else:
            print(0)
    elif "front" in oper:
        if q == []:
            print(-1)
        else:
            print(q[0])
    elif "back" in oper:
        if q == []:
            print(-1)
        else:
            print(q[-1])
