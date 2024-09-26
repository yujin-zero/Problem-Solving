import sys

n = int(sys.stdin.readline())
answer = 0
A = []
B = []
C = []
D = []
for _ in range(n) :
    a,b,c,d = map(int,sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

x = []
y = []

for i in range(n) :
    for j in range(n) :
        x.append(A[i] + B[j])

for i in range(n) :
    for j in range(n) :
        y.append(C[i] + D[j])

x.sort()
y.sort()

# 여기서 투포인터
left = 0
right = len(y)-1

while True :
    tmp = x[left] + y[right]
    if tmp == 0 :
        # 중복처리
        cnt_x = 1
        cnt_y = 1
        ll = left+1
        while ll < len(x) :
            if x[left] == x[ll] :
                cnt_x += 1
                left = ll
                ll += 1
            else :
                break
        rr = right-1
        while rr > -1 :
            if y[right] == y[rr] :
                cnt_y += 1
                right = rr
                rr -= 1 
            else :
                break

        answer += (cnt_x * cnt_y)
        if left < len(x) - 1:
            left += 1
        elif right > 0 :
            right -= 1
        else :
            break
    elif tmp < 0 :
        if left < len(x) - 1 :
            left += 1
        else :
            break
    else :
        if right > 0 :
            right -= 1
        else :
            break

print(answer)