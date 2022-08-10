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

T = int(input())
for tc in range(T):
    n = int(input())
    
    odd1 = n // 2
    odd2 = n - odd1
    for _ in range(n//2):
        if is_prime(odd1) == True and is_prime(odd2) == True:
            print(odd1, odd2)
            break
        else:
            odd1 -= 1
            odd2 += 1
            if odd1 < 2:
                print("Goldbach's conjecture is wrong.")
                break