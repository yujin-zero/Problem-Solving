def solution(participant, completion):
    people = dict()
    for c in completion :
        if c in people :
            people[c] += 1
        else :
            people[c] = 1
            
    for p in participant :
        if p not in people :
            return p
        
        people[p] -= 1
        if people[p] < 0 :
            return p