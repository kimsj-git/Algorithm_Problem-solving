N, M = map(int, input().split())

not_listen = set([input() for _ in range(N)])
not_seen = set([input() for _ in range(M)])

result = sorted(list(not_listen & not_seen))

print(len(result))
print(*result, sep='\n')