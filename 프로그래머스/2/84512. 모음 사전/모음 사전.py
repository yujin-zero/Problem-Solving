from itertools import permutations

def solution(search_word):
    lst = set()
    mo = ['A','A','A','A','A','E','E','E','E','E','I','I','I','I','I','O','O','O','O','O','U','U','U','U','U']
    
    for i in range(1,6) :
        words = list(permutations(mo,i))
        for word in words :
            w = "".join(word)
            lst.add(w)
    
    lst = list(lst)
    lst.sort()
    
    len_l = len(lst)
    for i in range(len_l) :
        if lst[i] == search_word :
            break
            
    return i+1