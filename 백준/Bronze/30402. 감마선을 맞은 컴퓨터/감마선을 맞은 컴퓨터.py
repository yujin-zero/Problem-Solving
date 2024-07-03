import sys

picture = []
for _ in range(15) :
    p = list(sys.stdin.readline().split())
    picture.append(p)

for i in range(15) :
    for j in range(15) :
        if picture[i][j] == 'w' :
            print("chunbae")
            sys.exit(0)
        elif picture[i][j] == 'b' :
            print("nabi")
            sys.exit(0)
        elif picture[i][j] == 'g' :
            print("yeongcheol")
            sys.exit(0)
