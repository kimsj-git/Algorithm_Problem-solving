def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    dp1 = [0] + sticker[:-1]
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
        
    dp2 = [0] + sticker[1:]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])
        
    return max(dp1[n-1], dp2[n-1])