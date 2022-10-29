decode = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}


def bin_to_code(chars):
    bin_codes = [chars[7*i: 7*(i+1)] for i in range(8)]
    result = ''
    for bin_code in bin_codes:
        result += decode[bin_code]
    
    return result


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
    
    # 행에서 마지막으로 나온 1을 끝으로 56개의 문자를 이진 코드로 저장
    bin_chars = ''
    flag = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                bin_chars = arr[i][j-55: j+1]
                flag = True
                break
        if flag:
            break
    print(f'#{tc} {verified_sum(bin_to_code(bin_chars))}')