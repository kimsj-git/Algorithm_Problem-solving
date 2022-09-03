N = int(input())
cola, beer = map(int, input().split())

chickens = cola // 2 + beer

if chickens <= N:
    print(chickens)
elif chickens > N:
    print(N)