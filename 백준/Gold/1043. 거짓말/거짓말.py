import sys

n, m = map(int,sys.stdin.readline().split())

x = list(map(int,sys.stdin.readline().split()))
knowTruth = set(x[1:len(x)])
party = []
people = [set() for _ in range(n+1)]
queue = []
visit = set()
cnt = 0

for i in range(m) :
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(x)) :
        people[x[j]].add(i)
        if x[j] in knowTruth :
            if i not in queue :
                queue.append(i)
                visit.add(i)
    party.append(set(x[1:len(x)]))

while queue :
    tmp = queue.pop()
    cnt += 1
    for a in party[tmp] :
        for b in people[a]:
            if b not in visit :
                visit.add(b)
                queue.append(b)


print(m-cnt)