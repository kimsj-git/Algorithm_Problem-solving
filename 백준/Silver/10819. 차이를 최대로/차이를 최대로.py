from collections import deque

N = int(input())
nums_input = list(map(int, input().split()))
nums1 = deque(sorted(nums_input))
nums2 = deque(sorted(nums_input))
dq1 = deque()
dq2 = deque() 

# 작은수 먼저 덱에 추가
idx = 0
while nums1:
    if idx % 4 == 0:
        dq1.appendleft(nums1.popleft())
    elif idx % 4 == 1:
        dq1.append(nums1.pop())
    elif idx % 4 == 2:
        dq1.appendleft(nums1.pop())
    elif idx % 4 == 3:
        dq1.append(nums1.popleft())
    idx += 1

result1 = 0
for i in range(N-1):
    result1 += abs(dq1[i] - dq1[i+1])

# 큰수 먼저 덱에 추가
idx = 0
while nums2:
    if idx % 4 == 0:
        dq2.appendleft(nums2.pop())
    elif idx % 4 == 1:
        dq2.append(nums2.popleft())
    elif idx % 4 == 2:
        dq2.appendleft(nums2.popleft())
    elif idx % 4 == 3:
        dq2.append(nums2.pop())
    idx += 1

result2 = 0
for i in range(N-1):
    result2 += abs(dq2[i] - dq2[i+1])

print(max(result1, result2))