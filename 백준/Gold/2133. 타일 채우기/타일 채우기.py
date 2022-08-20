N = int(input())

tiles = [0] * 31

tiles[2] = 3
tiles[4] = 11

def tiles_dp(n):
    if n < 6:
        return tiles[n]
    for i in range(6, n+1, 2):
        for j in range(2, i-2, 2):
            tiles[i] += tiles[j] * 2
        tiles[i] += tiles[i-2] * 3 + 2
    return tiles[n]

print(tiles_dp(N))