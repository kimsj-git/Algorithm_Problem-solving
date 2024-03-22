from collections import defaultdict


def dfs(n, node, graph, routes, route=[]):
    new_route = route + [node]
    if len(new_route) == n + 1:
        routes.append(new_route)
        return
    for next, tickets_left in graph[node].items():
        if tickets_left > 0:
            graph[node][next] -= 1
            dfs(n, next, graph, routes, new_route)
            graph[node][next] += 1

            
def solution(tickets):
    graph = defaultdict(lambda: defaultdict(lambda: 0))
    for ticket in tickets:
        start, end = ticket
        graph[start][end] += 1
    routes = []
    dfs(len(tickets), 'ICN', graph, routes)

    return min(routes)