T = int(input())

for tc in range(T):
    sentence = list(input().split())
    reversed_words = []
    for word in sentence:
        reversed_words.append(word[::-1])
    print(' '.join(reversed_words))
