import sys
import bisect

n = int(sys.stdin.readline())
input_line = []
for _ in range(n) :
    s, e = map(int,sys.stdin.readline().split())
    if s > e :
        t = s
        s = e
        e = t
    input_line.append((s,e))
d = int(sys.stdin.readline())
answer = 0

line = dict()
for s, e in input_line :
    if e-s > d :
        continue
    
    if e in line :
        line[e].append(s)
    else :
        line[e] = [s]

include = []
for end in sorted(line) :
    start = end - d
    
    while include :
        if include[0] < start :
            include.pop(0)
        else :
            break
    
    for s in line[end] :
        bisect.insort(include,s)

    answer = max(answer, len(include))

print(answer)
