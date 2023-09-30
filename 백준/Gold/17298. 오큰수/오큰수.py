import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nge = [-1] * N  # 오큰수 값 저장
stack = []  # 아직 오큰수를 찾지 못한 index 값 스택

for i in range(N):
    # nums[i] 값이 오큰수가 되는 index 값 찾기
    while stack and nums[stack[-1]] < nums[i]:
        nge[stack.pop()] = nums[i]
    stack.append(i)

print(*nge)
