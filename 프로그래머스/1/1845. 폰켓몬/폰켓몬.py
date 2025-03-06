def solution(nums):
    total_cnt = 0
    ponket_type = dict()
    for n in nums :
        if n not in ponket_type :
            ponket_type[n] = True
            total_cnt += 1
            
    if total_cnt >= len(nums) // 2 :
        return len(nums)//2
    else :
        return total_cnt