def solution(n, s):
    div = s // n

    if div < 1:
        return [-1]
    
    left = s % n
    answer = [div] * n
    for i in range(left):
        answer[-1 - i] += 1
    
    return answer