import sys

m1, m2 = sys.stdin.readline().rstrip().split('+')
m2, m3 = m2.split('=')
che = [m1,m2,m3]

# c,h,o
num = [[0,0,0],[0,0,0],[0,0,0]]
for j in range(3) :
    for i in range(len(che[j])):
        if che[j][i] == 'C' :
            num[j][0] += 1
            tmp = 'C'
        elif che[j][i] == 'H' :
            num[j][1] += 1
            tmp = 'H'
        elif che[j][i] == 'O' :
            num[j][2] += 1
            tmp = 'O'
        else :
            value = int(che[j][i]) -1 
            if tmp == 'C' :
                num[j][0] += value
            elif tmp == 'H' :
                num[j][1] += value
            else :
                num[j][2] += value

for i in range(1,11) :
    for j in range(1,11) :
        for k in range(1,11) :
            a1, b1, c1 = num[0]
            a2, b2, c2 = num[1]
            a3, b3, c3 = num[2]
            if (a1*i + a2*j == a3*k) and (b1*i + b2*j == b3*k) and (c1*i + c2*j == c3*k) :
                print(i,j,k)
                sys.exit(0)