import sys
input = sys.stdin.readline

while True:
    code = input().rstrip()
    if code == 'END':
        break
    print(code[::-1])