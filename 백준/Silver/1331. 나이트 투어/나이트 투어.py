import sys

visit = set()
first = sys.stdin.readline()
beX = ord(first[0])-ord('A')
beY = int(first[1])
visit.add((beX,beY))
possible = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

for _ in range(35) :
    x = sys.stdin.readline()
    a = ord(x[0])-ord('A')
    b = int(x[1])

    if (a,b) in visit :
        print("Invalid")
        sys.exit(0)

    tmp = False
    for (i,j) in possible :
        if beX+i == a and beY+j == b :
            tmp = True
            break
    
    if tmp :
        visit.add((a,b))
        beX = a
        beY = b
    else :
        print("Invalid")
        sys.exit(0)

a = ord(first[0])-ord('A')
b = int(first[1])

tmp = False
for (i,j) in possible :
    if beX+i == a and beY+j == b :
        tmp = True
        break
if tmp :
    print("Valid")
else :
    print("Invalid")