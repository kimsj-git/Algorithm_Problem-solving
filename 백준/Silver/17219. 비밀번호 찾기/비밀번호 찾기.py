import sys
input = sys.stdin.readline

N, M = map(int, input().split())
passwords = {}
for _ in range(N):
    url, pwd = input().strip().split()
    passwords[url] = pwd

searches = [input().strip() for _ in range(M)]
for search in searches:
    print(passwords[search])