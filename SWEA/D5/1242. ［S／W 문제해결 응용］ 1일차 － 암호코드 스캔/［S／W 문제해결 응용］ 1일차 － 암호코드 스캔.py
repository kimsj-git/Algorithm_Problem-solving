# 16진수 -> 2진수 변환
hex_dec = {f'{i}': i for i in range(10)}
hex_dec.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
def hex_to_bin(chars):
    result = ''
    for char in chars:
        num = hex_dec[char]
        temp = ''
        for _ in range(4):
            temp = str(num % 2) + temp
            num //= 2
        result += temp
    return result


# 이진코드 -> 검증코드 변환
decode = {'211': '0', '221': '1', '122': '2', '411': '3', '132': '4', '231': '5', '114': '6', '312': '7', '213': '8', '112': '9'}


def verified_sum(code):
    v_sum = 0
    for i in range(8):
        if i % 2:
            v_sum += int(code[i])
        else:
            v_sum += 3 * int(code[i])
    if v_sum % 10:
        return 0
    else:
        return sum(map(int, code))


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    
    v_codes = []
    for hex_row in arr:
        bin_row = hex_to_bin(hex_row).rstrip('0')
        if not bin_row:
            continue
        
        # print(bin_row)
        digit_cnt = 0
        v_code = ''
        c1 = c2 = c3 = 0
        for i in range(len(bin_row)-1, 0, -1):
            if bin_row[i] == '0'and c1 == 0:
                continue
            elif bin_row[i] == '1' and c2 == 0:
                c1 += 1
            elif bin_row[i] == '0' and c3 == 0:
                c2 += 1
            elif bin_row[i] == '1':
                c3 += 1
            elif bin_row[i] == '0' and c3:
                gcd = min(c1, c2, c3)
                c1 //= gcd
                c2 //= gcd
                c3 //= gcd
                # print(c3, c2, c1)
                v_code = decode[f'{c3}{c2}{c1}'] + v_code
                # print(v_code)
                digit_cnt += 1
                c1 = c2 = c3 = 0
                
                if digit_cnt == 8:
                    # print(v_code)
                    if v_code not in v_codes:
                        v_codes.append(v_code)
                    v_code = ''
                    digit_cnt = 0

    result = 0
    # print(v_codes)
    for v_code in v_codes:
        result += verified_sum(v_code)

    print(f'#{tc} {result}')
