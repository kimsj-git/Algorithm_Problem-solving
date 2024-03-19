def solution(n, tops):
    full = [0] * n
    not_full = [0] * n
    
    if tops[0] == 1:
        full[0], not_full[0] = 4, 3
    else:
        full[0], not_full[0] = 3, 2
    
    for i in range(1, n):
        if tops[i] == 1:
            full[i] = (full[i-1] * 3 + not_full[i-1] * 1) % 10007
            not_full[i] = (full[i-1] * 2 + not_full[i-1]) % 10007
        else:
            full[i] = (full[i-1] * 2 + not_full[i-1]) % 10007
            not_full[i] = (full[i-1] + not_full[i-1]) % 10007
    
    return full[n-1]