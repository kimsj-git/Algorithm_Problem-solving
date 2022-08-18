steps = [[0] * 10 for _ in range(101)]
steps[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def steps_dp(n):
    for i in range(2, n+1):
        steps[i][0] = steps[i-1][1]
        for j in range(1, 9):
            steps[i][j] = steps[i-1][j-1] + steps[i-1][j+1]
        steps[i][9] = steps[i-1][8]
    return steps[n]


N = int(input())
print(sum(steps_dp(N)) % 1000000000)