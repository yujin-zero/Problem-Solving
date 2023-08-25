import sys

lst = []
for _ in range(9):
    lst.append(int(sys.stdin.readline()))

lst.sort()
# print(sum(lst))
answer = sum(lst)-100
for i in range(9):
    for j in range(9):
        if i != j:
            if lst[i]+lst[j] == answer:
                for k in range(9):
                    if k != i and k != j:
                        print(lst[k])
                sys.exit()
