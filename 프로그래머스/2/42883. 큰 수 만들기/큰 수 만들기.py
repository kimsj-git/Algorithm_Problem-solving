def solution(number, k):
    n = len(number)
    stack = [number[0]]
    i = 1
    while k > 0 and i < n:
        if stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        else:
            stack.append(number[i])
            i += 1
    answer = ''.join(stack)

    if i < n:
        answer += number[i:]
    if k > 0:
        answer = answer[:-k]
    
    return answer
