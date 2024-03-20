from collections import defaultdict

def solution(edges):
    outbound = defaultdict(lambda: [])
    inbound = defaultdict(lambda: [])
    nodes = set([])
    for edge in edges:
        s, e = edge
        outbound[s].append(e)
        inbound[e].append(s)
        nodes.update({s, e})
    
    created_node = 0
    for node in outbound.keys():
        if len(outbound[node]) >= 2 and len(inbound[node]) == 0:
            created_node = node
            break

    total_graphs = len(outbound[created_node])
    straights = 0
    eights = 0
    for node in nodes:
        if node == created_node:
            continue
        if len(outbound[node]) == 2:
            eights += 1
        elif len(outbound[node]) == 0:
            straights += 1
    donuts = total_graphs - eights - straights
    
    return [created_node, donuts, straights, eights]