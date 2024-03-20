from itertools import combinations


def solution(friends, gifts):
    last_month = {friend: {} for friend in friends}
    for gift in gifts:
        giver, receiver = gift.split()
        if last_month[giver].get(receiver):
            last_month[giver][receiver] += 1
        else:
            last_month[giver][receiver] = 1
    
    gift_score = {friend: 0 for friend in friends}
    for giver, gift_to in last_month.items():
        for receiver, num in gift_to.items():
            gift_score[giver] += num
            gift_score[receiver] -= num
    
    this_month = {friend: 0 for friend in friends}
    for a, b in combinations(friends, 2):
        a_to_b = last_month[a].get(b) if last_month[a].get(b) else 0
        b_to_a = last_month[b].get(a) if last_month[b].get(a) else 0
        if a_to_b > b_to_a:
            this_month[a] += 1
        elif a_to_b < b_to_a:
            this_month[b] += 1
        elif gift_score[a] > gift_score[b]:
            this_month[a] += 1
        elif gift_score[b] > gift_score[a]:
            this_month[b] += 1
    
    return max(this_month.values())