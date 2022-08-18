def ops_dp(N):
    ops = [0] * 1000001
    ops[2] = 1
    ops[3] = 1
    for i in range(4, N+1):
        case1 = ops[i//3] if i%3 == 0 else 1000000
        case2 = ops[i//2] if i%2 == 0 else 1000000
        case3 = ops[i-1]
        best_case = min(case1, case2, case3)
        ops[i] = best_case + 1
    return ops[N]
                
N = int(input())
print(ops_dp(N))