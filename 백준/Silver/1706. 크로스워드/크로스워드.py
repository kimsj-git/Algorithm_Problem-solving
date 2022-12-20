import sys
input = sys.stdin.readline
R, C = map(int, input().split())

puzzle = [input().rstrip() for _ in range(R)]

words = []
# row scan
for r in range(R):
    word = ''
    for c in range(C):
        if puzzle[r][c] == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
        else:
            word += puzzle[r][c]
    if len(word) > 1:
        words.append(word)

# col scan
for c in range(C):
    word = ''
    for r in range(R):
        if puzzle[r][c] == '#':
            if len(word) > 1:
                words.append(word)
            word = ''
        else:
            word += puzzle[r][c]
    if len(word) > 1:
        words.append(word)

words.sort()
print(words[0])