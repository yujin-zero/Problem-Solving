def solution(brown, yellow):
    
    for yellow_width in range(yellow,0,-1) :
        if yellow % yellow_width != 0 :
            continue
    
        yellow_height = yellow // yellow_width
        
        if 2*yellow_width + 2*yellow_height + 4 == brown :
            break
            
    tmp1 = yellow_width + 2
    tmp2 = yellow_height + 2
    
    width = max(tmp1, tmp2)
    height = min(tmp1, tmp2)
    
    return [width, height]
            
            