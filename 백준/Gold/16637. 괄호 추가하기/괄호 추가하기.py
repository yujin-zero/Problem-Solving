import sys

def calculate(a,b,o) :
    if o == '+' :
        return a+b
    elif o == '-' :
        return a-b
    else :
        return a*b

def find_max(idx,pre_num) : 
    if idx >= N :
        result.append(pre_num)
        return

    oper = x[idx]
    num = int(x[idx+1])

    tmp = calculate(pre_num,num,oper)
    find_max(idx+2,tmp)

    if idx != N-2 :
        next_oper = x[idx+2]
        next_num = int(x[idx+3])
        t = calculate(num,next_num,next_oper)
        tmp = calculate(pre_num,t,oper)
        find_max(idx+4,tmp)
    else :
        result.append(tmp)

N = int(sys.stdin.readline())
x = list(sys.stdin.readline().rstrip())
result = []

find_max(1,int(x[0]))

print(max(result))