from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for dungeon_seq in permutations(dungeons, len(dungeons)):
        energy = k
        cnt = 0
        for dungeon in dungeon_seq:
            required_energy, consumed_energy = dungeon
            if energy >= required_energy:
                energy -= consumed_energy
                cnt += 1
            else:
                answer = max(answer, cnt)
                break
        answer = max(answer, cnt)
        
    return answer