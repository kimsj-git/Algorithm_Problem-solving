def solution(n, times):
    answer = 0
    s, e = 0, 10 ** 18
    while s <= e:
        mid = (s + e) // 2
        count = 0
        for time in times:
            count += mid // time

        if count < n:
            s = mid + 1
        else:
            answer = mid
            e = mid - 1

    return answer