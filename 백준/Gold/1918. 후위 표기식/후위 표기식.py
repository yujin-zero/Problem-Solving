import sys

def cal(xx,yy) :
    global result
    stack = []

    i = 0
    while i < len(xx) :
        value = xx[i]
        if value == '+' or value == '-' :
            while stack :
                result.append(stack.pop())
            stack.append(value)
        elif value == '*' or value == '/' :
            if stack:
                if stack[-1] == '*' or stack[-1] == '/' :
                    result.append(stack.pop())
            stack.append(value)
        elif value == '(' :
            end = part[i+yy]
            cal(xx[i+1:end-yy],i+yy+1)
            i = end-yy
        else :
            result.append(value)

        i += 1

    while stack :
        result.append(stack.pop())

    return result

x = list(sys.stdin.readline().rstrip())
result = []
part = dict()
tmp = []
for i in range(len(x)) :
    v = x[i]
    if v == '(' :
        tmp.append(i)
    elif v == ')' :
        tt = tmp.pop()
        part[tt] = i

answer = cal(x,0)
print(''.join(answer))