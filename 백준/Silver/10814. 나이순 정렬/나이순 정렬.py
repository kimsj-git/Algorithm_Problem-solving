import sys
input = sys.stdin.readline

N = int(input())
profiles = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    profiles.append([age, i, name])

profiles.sort(key=lambda x: (x[0], x[1]))
for profile in profiles:
    age, i, name = profile
    print(age, name)