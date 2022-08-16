N = int(input())

words_set = set(input() for _ in range(N))
words = list(words_set)

words.sort()
words.sort(key=len)

for word in words:
    print(word)
