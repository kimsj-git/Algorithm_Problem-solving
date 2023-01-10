from itertools import permutations as P

k = int(input())
brackets = list(input().split())

results = []
for nums in P(range(10), k+1):
    result = str(nums[0])
    for i in range(1, k+1):
        if brackets[i-1] == '<' and nums[i-1] < nums[i]:
            result += str(nums[i])
        elif brackets[i-1] == '>' and nums[i-1] > nums[i]:
            result += str(nums[i])
        else:
            break
    if len(result) == k+1:
        results.append(result)

print(results[-1])
print(results[0])