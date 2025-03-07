from itertools import permutations

def isSosu(x) :
    if x == 0 or x == 1 :
        return False
    
    for i in range(2, int(x**(1/2))+1) :
        if x % i == 0 :
            return False
        
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    lst = set()
    
    for repeat in range(1,len(numbers)+1) :
        for n in list(permutations(numbers, repeat)) :
            value = int("".join(n))
            lst.add(value)

    for l in lst :
        if isSosu(l) :
            answer += 1
    
    return answer