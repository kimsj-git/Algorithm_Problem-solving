table = {i:0 for i in range(65, 91)}

chars = input()
for char in chars:
    x = ord(char)
    if 65 <= x <= 90:
        table[x] += 1
    else:
        table[x - 32] += 1

result = sorted(table.items(), key=lambda x: -x[1])
if len(result) > 1 and result[0][1] == result[1][1]:
    print('?')
else:
    print(chr(result[0][0]))