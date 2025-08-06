def solution(participant, completion):
    answer = ''
    
    dictionary = dict()
    for c in participant :
        if c in dictionary :
            dictionary[c] += 1
        else :
            dictionary[c] = 1
            
    #print(dictionary)
    for c in completion :
        dictionary[c] -= 1
    #print(dictionary)
    for key, value in dictionary.items() :
        if value >= 1 :
            return key
        
    
    return answer