import sys

def CCW(a1,b1,a2,b2,a3,b3) :
    ccw = (a2-a1) * (b3-b1) - (b2-b1) * (a3-a1)
    return ccw

x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
x3,y3,x4,y4 = map(int,sys.stdin.readline().split())

abc = CCW(x1,y1,x2,y2,x3,y3)
abd = CCW(x1,y1,x2,y2,x4,y4)
cda = CCW(x3,y3,x4,y4,x1,y1)
cdb = CCW(x3,y3,x4,y4,x2,y2)

if abc * abd < 0 and cda * cdb < 0 :
    print(1)
elif abc == 0 and (min(x1,x2) <= x3 <= max(x1,x2) and min(y1,y2) <= y3 <= max(y1,y2)):
    print(1)
elif abd == 0 and (min(x1,x2) <= x4 <= max(x1,x2) and min(y1,y2) <= y4 <= max(y1,y2)):
    print(1)
elif cda == 0 and (min(x3,x4) <= x1 <= max(x3,x4) and min(y3,y4) <= y1 <= max(y3,y4)):
    print(1)
elif cdb == 0 and (min(x3,x4) <= x2 <= max(x3,x4) and min(y3,y4) <= y2 <= max(y3,y4)):
    print(1)
else :
    print(0)