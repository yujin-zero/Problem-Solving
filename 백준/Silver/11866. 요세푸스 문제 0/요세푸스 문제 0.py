import sys

n, k = map(int, sys.stdin.readline().split())
circle = []
result = []  # 정답

for i in range(1, n+1):
    circle.append(i)

j = 0
size = n
while circle != []:
    j += (k-1)
    while j > size-1:
        j -= size
    # print("j:", j)
    # print(circle[j])
    result.append(circle.pop(j))
    size -= 1

print("<", end='')
for i in range(n-1):
    print(result[i], end=', ')
print(result[n-1], end='')
print(">")
