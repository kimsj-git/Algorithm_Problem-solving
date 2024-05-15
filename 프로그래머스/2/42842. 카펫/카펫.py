import math

def solution(brown, yellow):
    total_area = brown + yellow
    width = math.ceil((total_area)**0.5)
    while width < total_area:
        height = (brown + 4 - 2 * width) / 2
        if width * height == total_area:
            return [width, height]
        width += 1