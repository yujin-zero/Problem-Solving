import sys

n, k = map(int, sys.stdin.readline().split())
queue = [i for i in range(1, n+1)]
answer = []

i = 0
while queue:
    i += (k-1)
    while i >= len(queue):
        i -= len(queue)
    x = queue.pop(i)
    answer.append(x)

print('<', end='')
for i in range(len(answer)-1):
    print(answer[i], end=', ')
print(answer[-1], end='')
print('>')
