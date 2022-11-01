for tc in range(1, 11):
    n, start = map(int, input().split())
    data = list(map(int, input().split()))

    graph = {i:[] for i in range(1, 101)}
    for i in range(n//2):
        graph[data[2*i]].append(data[2*i + 1])

    checked = [0] * 101
    
    queue = [start]
    checked[start] = 1
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if not checked[w]:
                checked[w] = checked[v] + 1
                queue.append(w)
    
    max_count = max(checked)
    for i in range(100, 0, -1):
        if checked[i] == max_count:
            result = i
            break

    print(f'#{tc} {result}')