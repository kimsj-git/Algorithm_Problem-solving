from collections import defaultdict


def solution(clothes):
    clothes_dict = defaultdict(lambda: 0)
    for name, clothes_type in clothes:
        clothes_dict[clothes_type] += 1
    
    result = 1
    for value in clothes_dict.values():
        result *= (value + 1)
    
    return result - 1