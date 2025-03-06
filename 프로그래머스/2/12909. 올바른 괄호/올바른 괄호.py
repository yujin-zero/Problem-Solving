def solution(s):
    stack = []
    
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append("(")
        else :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                return False
            
    if stack :
        return False
    
    return True