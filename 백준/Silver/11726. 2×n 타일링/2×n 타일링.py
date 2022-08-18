n = int(input())

recs = [1, 2]
def recs_dp(N):
    global recs
    for i in range(2, N):
        recs.append(recs[i-1] + recs[i-2])
    return recs[N-1]

print(recs_dp(n) % 10007)