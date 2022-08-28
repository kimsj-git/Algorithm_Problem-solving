from itertools import combinations
dwarves = [int(input()) for _ in range(9)]
dwarves.sort()

for combi in combinations(dwarves, 7):
    if sum(combi) == 100:
        print(*combi, sep='\n')
        break