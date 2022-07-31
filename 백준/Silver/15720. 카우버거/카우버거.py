import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())
burgers = sorted(list(map(int, input().split())),reverse=True)
sides = sorted(list(map(int, input().split())),reverse=True)
drinks = sorted(list(map(int, input().split())),reverse=True)

discounts = min(B, C, D)

price_total = 0
price_discount = 0

for idx, burger in enumerate(burgers):
    price_total += burger
    if idx < discounts:
        price_discount += int(burger * 0.9)
    else:
        price_discount += burger

for idx, side in enumerate(sides):
    price_total += side
    if idx < discounts:
        price_discount += int(side * 0.9)
    else:
        price_discount += side

for idx, drink in enumerate(drinks):
    price_total += drink
    if idx < discounts:
        price_discount += int(drink * 0.9)
    else:
        price_discount += drink

print(price_total)
print(price_discount)