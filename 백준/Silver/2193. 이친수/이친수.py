N = int(input())

pinary = [0] * 91
pinary[1] = 1
pinary[2] = 1


def pinary_dp(n):
    global pinary
    if n < 3:
        return pinary[n]
    for i in range(3, n+1):
        pinary[i] = pinary[i-1] + pinary[i-2]
    return pinary[n]

print(pinary_dp(N))