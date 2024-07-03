import sys

n, kim, lim = map(int,sys.stdin.readline().split())
find = [kim, lim]
tournament = [i for i in range(1,n+1)]
round = 1 
# tournament.pop(0) #index

while True :
    delete = set()
    for i in range(0,len(tournament), 2) :
        if i == len(tournament)-1 :
            break
        if (tournament[i] in find) and (tournament[i+1] in find) :
            print(round)
            sys.exit(0)
        elif tournament[i] in find :
            delete.add(i+1)
        else :
            delete.add(i)
    for i in range(len(tournament)-1,-1,-1) :
        if i in delete :
            tournament.pop(i)
    round += 1

