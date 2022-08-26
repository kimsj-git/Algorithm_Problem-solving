N = int(input())    # 스위치 개수
switches = list(map(int, input().split()))

M = int(input())    # 학생 수
for _ in range(M):
    # gender: 성별, num: 스위치 번호
    gender, num = map(int, input().split())
    
    if gender == 1:
        for i in range(N):
            if (i + 1) % num == 0:
                switches[i] =  (switches[i] + 1) % 2
    elif gender == 2:
        switches[num-1] =  (switches[num-1] + 1) % 2
        dx = 1
        while num - dx -1 >= 0 and num + dx - 1 < N:
            idx1 = num - dx - 1
            idx2 = num + dx - 1
            if switches[idx1] == switches[idx2]:
                switches[idx1] =  (switches[idx1] + 1) % 2
                switches[idx2] =  (switches[idx2] + 1) % 2
                dx += 1
            else:
                break

for i in range(1, N+1):
    print(switches[i-1], end=' ')
    if i % 20 == 0:
        print()