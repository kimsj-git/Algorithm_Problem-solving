from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        # cache hit
        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        # cache miss
        else:
            time += 5
            cache.append(city)
    return time