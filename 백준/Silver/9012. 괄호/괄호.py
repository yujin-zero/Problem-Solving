import sys

n = int(sys.stdin.readline())
# print(n)
brackets = []  # 괄호
result = []

for i in range(n):
    bracket = sys.stdin.readline()
    brackets.append(bracket)

for i in range(n):
    x = []
    x.append(brackets[i][0])
    for j in range(1, len(brackets[i])-1):
        if brackets[i][j] == '(':
            x.append('(')
        elif brackets[i][j] == ')':
            if len(x) != 0:
                if x[-1] == '(':
                    x.pop()
                elif x[-1] == ')':
                    x.append(')')
            else:
                x.append(')')
    if x == []:
        result.append("YES")
    else:
        result.append("NO")

for i in range(n):
    print(result[i])
