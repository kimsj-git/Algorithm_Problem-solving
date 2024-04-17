from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        count = 0
        for future_price in q:
            count += 1
            if price > future_price:
                break
        answer.append(count)
        
    return answer