def solution(s):
    answer = 1
    n = len(s)
    for i, char in enumerate(s):
        # 홀수 길이의 팰린드롬 검사
        left, right = i - 1, i + 1
        length_odd = 1
        while 0 <= left < n and 0 <= right < n:
            if s[left] == s[right]:
                length_odd += 2
                left, right = left - 1, right + 1
            else:
                break
        if length_odd > answer:
            answer = length_odd
        
        # 짝수 길이의 팰린드롬 검사
        if i < n - 1 and char == s[i + 1]:
            length_even = 2
            left, right = i - 1, i + 2
            while 0 <= left < n and 0 <= right < n:
                if s[left] == s[right]:
                    length_even += 2
                    left, right = left - 1, right + 1
                else:
                    break
            if length_even > answer:
                answer = length_even

    return answer