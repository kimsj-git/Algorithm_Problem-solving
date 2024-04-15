def solution(triangle):
    n = len(triangle)
    for i in range(n):
        if i == 0:
            continue
        triangle[i][0] += triangle[i-1][0]
        for j in range(1, i):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        triangle[i][i] += triangle[i-1][i-1]
    
    return max(triangle[n-1])