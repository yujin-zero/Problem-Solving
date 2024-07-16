import sys   
sys.setrecursionlimit(10**6)

def pop(start,end,tmp,kind) :
    global answer

    if end == n :
        print(answer)
        sys.exit(0)

    if tmp == 1 : # end 추가
        fruit[s[end]] += 1
        if fruit[s[end]] == 1 :
            kind += 1
    else : # start 뺌
        fruit[s[start-1]] -= 1 
        if fruit[s[start-1]] == 0:
            kind -= 1
    
    if kind <= 2 :
        answer = max(answer, end-start+1)
        return pop(start,end+1,1,kind)
    else :
        return pop(start+1,end,0,kind)



n = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))
answer = 0
fruit = [0] * 10
pop(0,0,1,0)
