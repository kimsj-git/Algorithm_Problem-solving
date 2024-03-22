def solution(numbers, target):
    answer = 0
    n = len(numbers)
    for i in range(1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += numbers[j]
            else:
                subset_sum -= numbers[j]
        if subset_sum == target:
            answer += 1
    
    return answer