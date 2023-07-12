import sys

n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    oper = sys.stdin.readline()

    if "push_front" in oper:
        x = int(oper.split()[1])
        deque.insert(0, x)
    elif "push_back" in oper:
        x = int(oper.split()[1])
        deque.append(x)
    elif "pop_front" in oper:
        if deque == []:
            print(-1)
        else:
            print(deque.pop(0))
    elif "pop_back" in oper:
        if deque == []:
            print(-1)
        else:
            print(deque.pop())
    elif "size" in oper:
        print(len(deque))
    elif "empty" in oper:
        if deque == []:
            print(1)
        else:
            print(0)
    elif "front" in oper:
        if deque == []:
            print(-1)
        else:
            print(deque[0])
    elif "back" in oper:
        if deque == []:
            print(-1)
        else:
            print(deque[-1])
