N = int(input())
nums = list(map(int, input().split()))

# 연속해서 커지는 최대 길이 구하기
max_1 = 1
cnt_1 = 1
for i in range(1, N):
    if nums[i] >= nums[i-1]:
        cnt_1 += 1
    else:
        cnt_1 = 1
    if cnt_1 > max_1:
        max_1 = cnt_1

# 연속해서 작아지는 최대 길이 구하기
max_2 = 1
cnt_2 = 1
for i in range(1, N):
    if nums[i] <= nums[i-1]:
        cnt_2 += 1
    else:
        cnt_2 = 1
    if cnt_2 > max_2:
        max_2 = cnt_2

print(max(max_1, max_2))