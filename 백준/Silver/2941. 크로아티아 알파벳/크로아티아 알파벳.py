import sys

x = sys.stdin.readline()
cnt = 0

i = 0
while i < len(x)-1:
    if x[i] == 'c':
        if x[i+1] == '=' or x[i+1] == '-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif x[i] == 'l':
        if x[i+1] == 'j':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif x[i] == 'n':
        if x[i+1] == 'j':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif x[i] == 's':
        if x[i+1] == '=':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif x[i] == 'z':
        if x[i+1] == '=':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif x[i] == 'd':
        if x[i+1] == 'z' and x[i+2] == '=':
            cnt += 1
            i += 3
        elif x[i+1] == '-':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    else:
        i += 1
        cnt += 1

print(cnt)
