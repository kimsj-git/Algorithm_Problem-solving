students = [i for i in range(1, 31)]
for _ in range(28):
    n = int(input())
    students.remove(n)

print(*sorted(students), sep='\n')