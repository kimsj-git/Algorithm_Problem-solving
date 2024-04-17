def solution(prices):
    length = len(prices)
    
    # 끝까지 가격이 떨어지지 않는 경우의 값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]
    
    # prices를 순회하며 현재 가격과 과거 가격을 비교, 현재 가격이 더 높으면 과거 가격을 업데이트
    stack = [0]     # prices에 대한 인덱스
    for i in range (1, length):
        # prices[i]: 현재 가격
        # prices[stack[-1]]: 과거 가격. stack에서 값을 pop할수록 더 과거로 돌아간다.
        while stack and prices[stack[-1]] > prices[i]:
            # 현재 가격보다 과거 가격이 높으면
            j = stack.pop()     # 이전 인덱스를 꺼내서
            answer[j] = i - j   # 이전 인덱스의 answer 값을 업데이트함. 꺼내졌다는건 미래에 가격이 떨어졌다는 뜻.
        stack.append(i)
    
    return answer
