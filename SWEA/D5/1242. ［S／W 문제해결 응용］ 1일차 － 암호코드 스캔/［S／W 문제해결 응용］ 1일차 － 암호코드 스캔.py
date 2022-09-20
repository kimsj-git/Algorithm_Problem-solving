# 16진수 -> 2진수 변환 함수
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


# 이진코드 -> 암호코드 변환 딕셔너리
decode = {'211': '0', '221': '1', '122': '2', '411': '3', '132': '4', '231': '5', '114': '6', '312': '7', '213': '8', '112': '9'}


# 유효한 암호코드의 합을 반환하는 함수
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
    
    v_codes = []    # 암호코드(8자리)들을 저장하는 리스트
    for hex_row in arr:
        # 16진수 행을 2진수 행으로 변환, 오른쪽 '0' 제거
        bin_row = hex_to_bin(hex_row).rstrip('0')
        
        # 행의 모든 요소가 0이면 rstrip('0')에 의해 2진수 행은 없어짐
        if not bin_row:
            continue
        
        digit_cnt = 0   # 암호코드의 자리수를 카운트
        v_code = ''     # 암호코드를 저장
        
        # 2진수 행을 뒤에서부터 순회하며 암호코드 구하기
        c1 = c2 = c3 = 0    # c1: 맨뒤 1의 개수, c2: 중간 0의 개수, c3: 첫번째 1의 개수
                            # 예시) '0001101'은 c1 = 1, c2 = 0, c3 = 2
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
                gcd = min(c1, c2, c3)       # 암호코드의 두께
                c1 //= gcd
                c2 //= gcd
                c3 //= gcd
                
                # 암호코드를 구하기: decode 딕셔너리 이용
                v_code = decode[f'{c3}{c2}{c1}'] + v_code

                digit_cnt += 1
                c1 = c2 = c3 = 0
                
                # 암호코드가 8자리가 되면 암호코드들을 모아놓는 리스트에 추가
                if digit_cnt == 8:
                    if v_code not in v_codes:
                        v_codes.append(v_code)
                    v_code = ''
                    digit_cnt = 0

    result = 0
    for v_code in v_codes:
        result += verified_sum(v_code)

    print(f'#{tc} {result}')
