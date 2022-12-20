import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

s = 0
e = 1
subseq = {nums[0]: 1}
maxL = 1
subL = 1
while True:
    if e == N:
        break

    if subseq.get(nums[e]) == None:
        subseq[nums[e]] = 1
        e += 1
        subL += 1
        if subL > maxL:
            maxL = subL
        # print(maxL, subseq)
    elif subseq.get(nums[e]) < K:
        subseq[nums[e]] += 1
        e += 1
        subL += 1
        if subL > maxL:
            maxL = subL
        # print(maxL, subseq)
    else:
        subseq[nums[s]] -= 1
        s += 1
        subL -= 1
        # print(maxL, subseq)

print(maxL)