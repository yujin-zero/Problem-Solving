import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
answer = []
for _ in range(n):
    x = sys.stdin.readline()

    if "push" in x:
        y = x.split()[1]
        queue.append(y)
    elif "pop" in x:
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif "size" in x:
        answer.append(len(queue))
    elif "empty" in x:
        if queue:
            answer.append(0)
        else:
            answer.append(1)
    elif "front" in x:
        if queue:
            answer.append(queue[0])
        else:
            answer.append(-1)
    else:
        if queue:
            answer.append(queue[-1])
        else:
            answer.append(-1)

for a in answer:
    print(a)
