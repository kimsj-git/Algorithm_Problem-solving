N = int(input())


def nqueen(row, cols):
    global count

    if row == N:
        count += 1
        return

    for c in range(N):
        if c in cols:
            continue

        nr, nc = row, c
        is_diag = False
        for qr, qc in enumerate(cols):
            if abs(nr - qr) == abs(nc - qc):
                is_diag = True
                break
        if not is_diag:
            nqueen(row + 1, cols + [nc])


count = 0
for i in range(N):
    nqueen(1, [i])

print(count)
