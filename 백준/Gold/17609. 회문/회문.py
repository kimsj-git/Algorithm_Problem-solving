import sys
input = sys.stdin.readline


def is_palindrome(chars):
    n = len(chars)
    for i in range(n//2):
        if chars[i] != chars[n - i - 1]:
            return False
    else:
        return True


def pal_or_palLike(chars):
    s = 0
    e = len(chars) - 1
    while s < e:
        # 두 포인터가 가리키는 문자가 같은 경우
        if chars[s] == chars[e]:
            s += 1
            e -= 1
        # 두 포인터가 가리키는 문자가 다른 경우
        else:
            if is_palindrome(chars[s:e]):
                return 1
            if is_palindrome(chars[s+1:e+1]):
                return 1
            return 2
    return 0



T = int(input())
words = [input().rstrip() for _ in range(T)]

for word in words:
    print(pal_or_palLike(word))