N = int(input())
A = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

# average time complexity for set is O(n)
for num in nums:
    if num in A:
        print(1)
    else:
        print(0)