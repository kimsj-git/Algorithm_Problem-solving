import copy
N = int(input())    # 주사위 개수
dices = [list(map(int, input().split())) for _ in range(N)]

sums_sides = []
for num in dices[0]:
    sides = copy.deepcopy(dices)
    n1 = num    # 아래칸 숫자
    max_side = 0
    for side in sides:
        idx_n1 = side.index(n1)
        
        if idx_n1 in [0, 5]:
            idx_n2 = 5 - idx_n1
        
        elif idx_n1 in [1, 3]:
            idx_n2 = 4 - idx_n1
        
        elif idx_n1 in [2, 4]:
            idx_n2 = 6 - idx_n1
        
        n2 = side[idx_n2]
        side.remove(n1)
        side.remove(n2)
        
        max_num = max(side)
        max_side += max_num
        n1 = n2                 # 윗칸 숫자를 다음 주사위의 아래칸 숫자로 저장
    
    sums_sides.append(max_side)

print(max(sums_sides))