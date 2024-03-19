from itertools import combinations


def solution(dice):
    answer = []
    max_win = 0
    for comb in combinations(range(len(dice)), len(dice) // 2):
        dices_a = [i for i in comb]
        dices_b = [i for i in range(len(dice)) if i not in comb]
        
        # a 주사위 세트의 합 빈도 구하기
        first_dice_a = dice[dices_a[0]]
        sums_count_a = {}
        for dice_num in first_dice_a:
            if sums_count_a.get(dice_num):
                sums_count_a[dice_num] += 1
            else:
                sums_count_a[dice_num] = 1
        for dice_idx in dices_a[1:]:
            dice_nums = dice[dice_idx]
            updated_sums_count = {}
            for dice_num in dice_nums:
                for prev_sum in sums_count_a.keys():
                    if updated_sums_count.get(prev_sum + dice_num):
                        updated_sums_count[prev_sum + dice_num] += sums_count_a[prev_sum]
                    else:
                        updated_sums_count[prev_sum + dice_num] = sums_count_a[prev_sum]
            sums_count_a = updated_sums_count
        
        # b 주사위 세트의 합 빈도 구하기
        first_dice_b = dice[dices_b[0]]
        sums_count_b = {}
        for dice_num in first_dice_b:
            if sums_count_b.get(dice_num):
                sums_count_b[dice_num] += 1
            else:
                sums_count_b[dice_num] = 1
        for dice_idx in dices_b[1:]:
            dice_nums = dice[dice_idx]
            updated_sums_count = {}
            for dice_num in dice_nums:
                for prev_sum in sums_count_b.keys():
                    if updated_sums_count.get(prev_sum + dice_num):
                        updated_sums_count[prev_sum + dice_num] += sums_count_b[prev_sum]
                    else:
                        updated_sums_count[prev_sum + dice_num] = sums_count_b[prev_sum]
            sums_count_b = updated_sums_count
        
        # a 주사위 세트의 승패 결과 계산
        win = tie = lose = 0
        for sum_a, count_a in sums_count_a.items():
            for sum_b, count_b in sums_count_b.items():
                count = count_a * count_b
                if sum_a > sum_b:
                    win += count
                elif sum_a == sum_b:
                    tie += count
                else:
                    lose += count
        
        # max_count와 비교하여 업데이트
        if win > max_win:
            answer = [i + 1 for i in dices_a]
            max_win = win
        
    return answer