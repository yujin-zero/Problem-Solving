import sys

def CCW(a1,b1,a2,b2,a3,b3) :
    ccw = (a2-a1)*(b3-b1) - (b2-b1)*(a3-a1)
    return ccw

x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
x3,y3,x4,y4 = map(int,sys.stdin.readline().split())

abc = CCW(x1,y1,x2,y2,x3,y3)
abd = CCW(x1,y1,x2,y2,x4,y4)
cda = CCW(x3,y3,x4,y4,x1,y1)
cdb = CCW(x3,y3,x4,y4,x2,y2)

if abc*abd < 0 and cda*cdb < 0 :
    print(1)
else :
    print(0)