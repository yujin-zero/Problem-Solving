t = int(input())
answer = []

for i in range(1,t+1) :
    n, k = map(int,input().split())
    grade = []

    for j in range(1,n+1) :
        a,b,c = map(int,input().split())
        total = a*0.35 + b*0.45 + c*0.2
        grade.append((j,total))
    grade.sort(key= lambda x: x[1],reverse= True)
    # 몇 등인지 구하자 -> rank 0부터
    for j in range(n) :
        if grade[j][0] == k :
            rank = j
    x = n/10
    # 등급을 구하자
    y = rank//x
    
    if y==0 :
        tmp = 'A+'
    elif y==1 :
        tmp = 'A0'
    elif y==2 : 
        tmp = 'A-'
    elif y==3 :
        tmp = 'B+'
    elif y==4 :
        tmp = 'B0'
    elif y==5 :
        tmp = 'B-'
    elif y==6 :
        tmp = 'C+'
    elif y==7 :
        tmp = 'C0'
    elif y==8 :
        tmp = 'C-'
    else:
        tmp = 'D0'
    
    answer.append(tmp)

for i in range(t) :
    print('#%d %s' % (i+1,answer[i]))