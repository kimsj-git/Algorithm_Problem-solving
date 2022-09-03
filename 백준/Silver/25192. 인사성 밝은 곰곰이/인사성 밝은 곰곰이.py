N = int(input())
chats = [input() for _ in range(N)]

i = 0
result = 0
gomgoms = set()
while i < N:
    if chats[i] == 'ENTER':
        result += len(gomgoms)
        gomgoms.clear()
    else:
        gomgoms.add(chats[i])
    i += 1
result += len(gomgoms)

print(result)