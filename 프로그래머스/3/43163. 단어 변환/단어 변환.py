from collections import deque


def is_changeable(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if begin not in words:
        words.append(begin)
    
    graph = {word: [] for word in words}
    for word in words:
        for other_word in words:
            if is_changeable(word, other_word):
                graph[word].append(other_word)
    
    visited = set([begin])
    q = deque([(begin, 0)])
    while q:
        now, cnt = q.popleft()
        for next in graph[now]:
            if next not in visited: 
                if next == target:
                    return cnt + 1
                q.append((next, cnt + 1))
                visited.add(next)
    
    return 0