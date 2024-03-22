def solution(routes):
    for route in routes:
        route.sort()
    routes.sort()

    count = 1
    camera = routes[0][0]
    start, end = routes[0]
    for route in routes:
        s, e = route
        if start <= s and e <= end:
            camera = e
            start, end = s, e
        elif s <= end and e > end:
            start = s
        elif end < s:
            count += 1
            camera = e
            start, end = s, e
    
    return count