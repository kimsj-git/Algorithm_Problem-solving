def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        prime = True
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                prime = False
                break
        return prime

while True:
    n = int(input())
    if n == 0:
        break

    odd1 = 3
    odd2 = n-3
    for i in range(n//2):
        if is_prime(odd1) == True and is_prime(odd2) == True:
            print(f'{n} = {odd1} + {odd2}')
            break
        else:
            odd1 += 2
            odd2 -= 2
            if odd1 > odd2:
                print("Goldbach's conjecture is wrong.")
                break