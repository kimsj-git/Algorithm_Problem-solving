N = int(input())

arr = [[0] * N for _ in range(N)]
graph = {}

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(N**2):
    student, *args = map(int, input().split())
    likes = [*args]
    graph[student] = likes

    likes_max = 0
    vacancies_max = 0
    
    locations = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                likes_cnt = 0
                vacancies_cnt = 0
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] in likes:
                            likes_cnt += 1
                        elif arr[nr][nc] == 0:
                            vacancies_cnt += 1
                if likes_cnt > likes_max:
                    likes_max = likes_cnt
                    vacancies_max = vacancies_cnt
                    locations = [(r, c)]
                elif likes_cnt == likes_max:
                    if vacancies_cnt > vacancies_max:
                        vacancies_max = vacancies_cnt
                        locations = [(r, c)]
                    elif vacancies_cnt == vacancies_max:
                        locations.append((r, c))
                
    locations.sort(key=lambda x: [x[0], x[1]])
    x, y = locations[0]
    arr[x][y] = student

result = 0
for r in range(N):
    for c in range(N):
        student = arr[r][c]
        cnt = 0
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] in graph[student]:
                    cnt += 1
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)