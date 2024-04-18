'''
[6, 5, 5, 5, 3, 3, 1, 0] -> 4
'''
def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    answer = 0
    for i in range(n):
        # h-index는 i + 1
        if citations[i] >= i + 1:
            answer = i + 1
        else:
            break
    return answer