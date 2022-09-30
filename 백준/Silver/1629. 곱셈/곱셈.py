A, B, C = map(int, input().split())


def recursive_power(x, n, c):
    if n == 1:
        return x % c
    if n % 2 == 0:
        temp = recursive_power(x, n//2, c)
        return (temp**2) % c
    else:
        temp = recursive_power(x, n//2, c)
        return (temp**2 * x) % c


print(recursive_power(A, B, C))