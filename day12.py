#!/usr/bin/env python3
sample = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

def reachable(graph, k, visited):
    if k == 0:
        return True
    if 0 in graph[k]:
        return True
    if k in visited:
        return False
    return any(map(lambda x: reachable(graph, x, visited + [k]), graph[k]))

def build_graph(in_txt): 
    graph = {}
    for l in in_txt.split('\n'):
        parts = l.split(' ')
        graph[int(parts[0])] = list(map(lambda x: int(x.strip(',')), parts[2:]))
    return graph
 
def num_connections(in_txt):
    graph = build_graph(in_txt)
    return sum([reachable(graph, k, []) for k in graph.keys()])
    

def docolor(colors, k, color, graph):
    if k in colors:
        return
    colors[k] = color
    for newk in graph[k]:
        docolor(colors, newk, color, graph)
    
def num_groups(in_txt):
    graph = build_graph(in_txt)
    colors = {}
    [docolor(colors, k, k, graph) for k in graph.keys()]
    return len(set(list(colors.values())))

if __name__ == "__main__":
    assert(num_connections(sample) == 6)
    assert(num_groups(sample) == 2)
    with open("12_in.txt") as f:
        text = f.read().strip()
        print("Part 1: {0}".format(num_connections(text)))
        print("Part 2: {0}".format(num_groups(text)))
