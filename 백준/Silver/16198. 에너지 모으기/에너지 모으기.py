from itertools import permutations

N = int(input())
energy = list(map(int, input().split()))

result = 0
for orders in permutations(list(range(1, N-1)), N-2):
    visited = [False] * (N+1)
    temp = 0
    for idx in orders:
        i1 = idx - 1
        i2 = idx + 1
        while True:
            if not visited[i1]:
                energy1 = energy[i1]
                break
            i1 -= 1
        while True:
            if not visited[i2]:
                energy2 = energy[i2]
                break
            i2 += 1
        visited[idx] = True
        temp += energy1 * energy2
    if temp > result:
        result = temp
print(result)
