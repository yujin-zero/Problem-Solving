import sys


n = int(sys.stdin.readline())
x = list(sys.stdin.readline().strip())
resultIndex = []
stack = []
stack2 = []

for i in range(n):
    if x[i] == '(':
        stack.append('(')
        stack2.append(i)
    else:
        if stack:
            if stack[-1] == '(':
                stack.pop()
                resultIndex.append(stack2.pop())
                resultIndex.append(i)
            else:
                stack.append(')')
                tmp = 0
        else:
            stack.append(')')
            tmp = 0

answer = 0
tmp = 0
z = len(resultIndex)
resultIndex.sort()

for i in range(1, z):
    if resultIndex[i] == resultIndex[i-1]+1:
        tmp += 1
        if tmp > answer:
            answer = tmp
    else:
        tmp = 0

if answer == 0:
    print(0)
else:
    print(answer+1)
