import sys
n = int(sys.stdin.readline())
stack = []
i = 1
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    while i <= x:
        stack.append(i)
        result.append('+')
        i += 1

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        sys.exit()

print('\n'.join(result))