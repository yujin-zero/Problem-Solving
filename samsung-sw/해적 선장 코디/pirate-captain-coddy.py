## T: 명령 갯수
import heapq

## 공격 준비
def attack_ready(input_list) :
    N = input_list[1]
    for i in range(N) :
        id, p, r = input_list[2 + i*3: 2+i*3 + 3]
        ship[id] = [p, r, True, 0]
        heapq.heappush(powerful_heap, (-p, id))
    return

## 지원 요청
def request_support(input_list) :
    id, p, r = input_list[1:4]
    ship[id] = [p, r, True, 0]
    heapq.heappush(powerful_heap, (-p, id))
    return

## 함포 교체
def replace_run_barrel(input_list) :
    id, pw = input_list[1:3]
    ship[id][0] = pw
    if not ship[id][2] :
        return
    heapq.heappush(powerful_heap, (-pw, id))
    return

## 공격 명령
def attak_command() :
    global current_time
    attack_cnt = 0
    real_attack_id_list = []
    total_attack = 0
    while powerful_heap :
        p, id = heapq.heappop(powerful_heap)
        p *= -1
        if ship[id][0] != p or not ship[id][2] :
            continue
        real_attack_id_list.append(id)
        total_attack += p
        ship[id][2] = False
        ship[id][3] = ship[id][1]
        heapq.heappush(ready_time, (current_time + ship[id][1], id))
        attack_cnt += 1
        if attack_cnt >= 5 :
            break
    print(total_attack, attack_cnt, *real_attack_id_list)
    return

def update_time() :
    global current_time
    while ready_time :
        if ready_time[0][0] > current_time :
            break
        tmp, id = heapq.heappop(ready_time)
        ship[id][2] = True
        heapq.heappush(powerful_heap, (-ship[id][0],id))
    return


T = int(input())
## id: 고유번호, p: 공격력, r: 재장전 시간, is_ready: 사격 준비 완료 여부, down_time: 재장전 완료까지 남은 시간
ship = dict()
powerful_heap = []
ready_time = []
for current_time in range(T) :
    if current_time != 0 :
        update_time()
    input_list = list(map(int, input().split()))
    command_type = input_list[0]
    if command_type == 100 :
        attack_ready(input_list)
    elif command_type == 200 :
        request_support(input_list)
    elif command_type == 300 :
        replace_run_barrel(input_list) 
    else:
        attak_command()

