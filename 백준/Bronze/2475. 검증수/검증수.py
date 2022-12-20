nums = map(int, input().split())
result = 0
for num in nums:
    result += num ** 2
print(result % 10)