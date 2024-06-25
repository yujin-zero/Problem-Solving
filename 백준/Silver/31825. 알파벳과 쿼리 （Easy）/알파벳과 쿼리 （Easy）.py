import sys

n, q = map(int,sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())

for _ in range(q) :
    a,b,c = map(int,sys.stdin.readline().split())

    if a == 1:
        bunch = 0
        for i in range(b,c) :
            if s[i] != s[i-1] :
                bunch += 1
        print(bunch+1)
    else :
        for i in range(b-1,c) :
            if s[i] == 'Z' :
                s[i] = 'A'
            else :
                s[i] = chr(ord(s[i])+1)
