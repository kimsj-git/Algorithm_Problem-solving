def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    answer = max(width) * max(height)
    return answer