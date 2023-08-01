import sys
import math

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree.sort(reverse=True)

treeDict = {}
for t in tree:
    if t in treeDict:
        treeDict[t] += 1
    else:
        treeDict[t] = 1

height = 0  # 현재까지 자른 나무 길이의 합
cut = max(tree)  # 자를 높이
count = 0

for t in treeDict:
    if (cut-t)*count + height < m:
        height += (cut-t)*count
        cut = t
    elif (cut-t)*count + height == m:
        break
    else:
        x = m-height  # 부족한 나무길이
        y = math.ceil(x/count)  # 줄어든 높이
        cut -= y
        height = m
        break

    count += treeDict[t]


if height < m:
    cut -= math.ceil((m-height)/count)

print(cut)
