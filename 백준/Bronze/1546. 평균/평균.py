N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
acc = 0
for score in scores:
    acc += score / max_score * 100
print(acc/N)