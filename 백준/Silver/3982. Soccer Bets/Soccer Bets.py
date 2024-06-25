import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    country = dict()
    for _ in range(16) :
        c1, c2, score1, score2 = sys.stdin.readline().split()
        if int(score1) > int(score2) :
            if c1 in country :
                country[c1] += 1
            else:
                country[c1] = 1
        else :
            if c2 in country :
                country[c2] += 1
            else:
                country[c2] = 1
    
    for c in country :
        if country[c] == 4 :
            print(c)
            break