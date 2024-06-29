import sys

while True :
    n = int(sys.stdin.readline())
    if n==0 :
        break
    page = list(sys.stdin.readline().rstrip().split(','))
    visit = set()
    for p in page :
        if '-' in p :
            low, high = map(int,p.split('-'))
            if low <= high :
                for i in range(low,high+1):
                    if i not in visit :
                        visit.add(i)
        else :
            if int(p) not in visit :
                visit.add(int(p))
    answer = len(visit)
    for v in visit :
        if v > n :
            answer -= 1
    print(answer)
