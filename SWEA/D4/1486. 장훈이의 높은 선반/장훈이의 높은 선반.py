T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    min_tower = sum(heights)
    
    for i in range(1 << N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += heights[j]
        
        if B <= temp < min_tower:
            min_tower = temp
    
    print(f'#{tc} {min_tower - B}')