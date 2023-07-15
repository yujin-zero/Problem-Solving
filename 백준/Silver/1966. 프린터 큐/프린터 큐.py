import sys

num = int(sys.stdin.readline())

for _ in range(num):
    n, k = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    i = 0
    while queue != []:
        if any(x > queue[0] for x in queue):
            y = queue.pop(0)
            queue.append(y)
            if k == 0:
                k = len(queue)-1
            else:
                k -= 1
        else:
            queue.pop(0)
            i += 1
            if k == 0:
                print(i)
                break
            else:
                k -= 1
