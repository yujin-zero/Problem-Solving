import sys

result = []
while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    stack = []
    for char in line:
        if char == '[':
            stack.append('[')
        elif char == '(':
            stack.append('(')
        elif char == ']':
            if stack != []:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
            else:
                stack.append(']')
        elif char == ')':
            if stack != []:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
            else:
                stack.append(')')
    if stack:
        result.append("no")
    else:
        result.append("yes")

for r in result:
    print(r)
