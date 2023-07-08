def solution(X, Y):
    answer = ''
    dict_x = {str(i): 0 for i in range(10)}
    dict_y = {str(i): 0 for i in range(10)}
    for char in X:
        dict_x[char] += 1
    for char in Y:
        dict_y[char] += 1
    
    for char, cnt_x in dict_x.items():
        cnt_y = dict_y[char]
        if cnt_x > 0 and cnt_y > 0:
            cnt_common = min(cnt_x, cnt_y)
            answer = char * cnt_common + answer
    
    if answer == '':
        return '-1'
    
    if answer[0] == '0':
        answer = '0'
    
    return answer