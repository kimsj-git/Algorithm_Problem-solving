import sys
input = sys.stdin.readline

def is_groupword(word):
    charlist = []
    result = True
    for char in word:
        if char not in charlist:
            charlist.append(char)
        else:
            if char == charlist[-1]:
                continue
            else:
                result = False
                break
    return result

N = int(input())
count = 0
for _ in range(N):
    word = input()
    if is_groupword(word):
        count += 1

print(count)