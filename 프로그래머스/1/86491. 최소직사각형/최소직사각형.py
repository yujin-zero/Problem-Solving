def solution(sizes):
    weight = 0 
    height = 0
    
    for s in sizes :
        weight = max(weight, max(s))
        height = max(height, min(s))
        
    return weight * height