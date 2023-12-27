import sys
import heapq

n = int(sys.stdin.readline())

for i in range(n):
    m = int(sys.stdin.readline())
    minQueue = []
    maxQueue = []
    num = dict()

    for j in range(m):
        x, y = sys.stdin.readline().split()
        y = int(y)

        if "I" in x:
            heapq.heappush(minQueue, y)
            heapq.heappush(maxQueue, -y)
            if y in num:
                num[y] += 1
            else:
                num[y] = 1

        elif "D" in x:
            if len(num) > 0:
                if y == -1:
                    while True:
                        delete = heapq.heappop(minQueue)
                        if delete in num:
                            num[delete] -= 1
                            if num[delete] == 0:
                                del num[delete]
                            break

                elif y == 1:
                    while True:
                        delete = -heapq.heappop(maxQueue)
                        if delete in num:
                            num[delete] -= 1
                            if num[delete] == 0:
                                del num[delete]
                            break

        # print(num)

    if num:
        while True:
            delete = heapq.heappop(minQueue)
            if delete in num:
                min = delete
                break
        while True:
            delete = -heapq.heappop(maxQueue)
            if delete in num:
                max = delete
                break
        print(max, min)
    else:
        print("EMPTY")
