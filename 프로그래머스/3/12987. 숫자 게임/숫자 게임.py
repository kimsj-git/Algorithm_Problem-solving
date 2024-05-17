def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    wins = 0
    i = 0
    while A:
        a_score = A.pop()
        if B[i] > a_score:
            wins += 1
            i += 1
    return wins