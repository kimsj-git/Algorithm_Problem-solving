lines = ''
while True:
    try:
        line = input()
        lines += line
    except EOFError:
        break

numbers = list(map(int, lines.split(',')))

print(sum(numbers))