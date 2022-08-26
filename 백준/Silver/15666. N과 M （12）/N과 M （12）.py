import itertools

N, M = map(int, input().split())
nums_input = list(map(int, input().split()))

select_from = list(set(nums_input))
select_from.sort()

results = list(itertools.combinations_with_replacement(select_from, M))
for result in results:
    print(' '.join(map(str, result)))