import sys

math = sys.stdin.readline().rstrip()
num = []
i = 0
temp = 0
for m in math:
    if m == '+':
        num.append(temp)
        num.append('+')
        temp = 0
    elif m == '-':
        num.append(temp)
        num.append('-')
        temp = 0
    else:
        temp = temp*10 + int(m)
num.append(temp)

answer = 0
sign = 1  # 0:뺄셈 1:덧셈
for n in num:
    if n == '-':
        sign = 0
    elif n != '+':
        if sign == 1:
            answer += n
        else:
            answer -= n
print(answer)
