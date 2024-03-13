def solution(nums):
    nums_set = set(nums)
    if len(nums_set) <= len(nums) / 2:
        return len(nums_set)
    else:
        return len(nums) / 2
