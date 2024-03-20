from itertools import combinations


def pairs_count(card_list, target_sum):
    result = 0
    for pair in combinations(card_list, 2):
        if sum(pair) == target_sum:
            result += 1
    return result


def solution(coin, cards):
    n = len(cards)
    
    my_cards = cards[:n//3] # 내가 가진 카드
    candidates = []         # 코인을 내고 교환할 수 있는 후보 카드
    
    my_pairs = pairs_count(my_cards, n + 1) # 내 카드 중 합이 n+1인 페어의 개수
    match_my_cards = 0      # 후보 카드 중 내 카드와 합이 n+1인 카드의 개수
    match_candidates = 0    # 후보 카드 중 합이 n+1인 페어의 개수
    
    round = 1
    for i in range(n//3, n, 2):
        two_cards = cards[i:i+2]
        candidates += two_cards
        for card in two_cards:
            if n + 1 - card in my_cards:
                match_my_cards += 1
            elif n + 1 - card in candidates:
                match_candidates += 1
        
        if my_pairs > 0:
            my_pairs -= 1
            round += 1
        elif match_my_cards > 0 and coin >= 1:
            match_my_cards -= 1
            coin -= 1
            round += 1
        elif match_candidates > 0 and coin >= 2:
            match_candidates -= 1
            coin -= 2
            round += 1
        else:
            return round

    return round
            