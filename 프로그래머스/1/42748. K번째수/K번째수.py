def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        sorted_sub_array = sorted(array[i-1:j])
        answer.append(sorted_sub_array[k-1])
    return answer