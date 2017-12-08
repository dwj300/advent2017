#!/usr/bin/env python3
sample = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

class Disk():
    def __init__(self, name, weight):
        self.children = {}
        self.name = name
        self.weight = weight
        self.childrensum = 0
    def __repr__(self):
        return "name: {0},weight: {1}, childweight: {2}, Children: {3} ".format(self.name, self.weight, self.childrensum, ["{0},".format(x) for x in self.children.values()])

def build_graph(in_txt):
    lines = in_txt.split('\n')
    disks = {}
    graph = {}
    for line in lines:
        if "->" in line:
            parts = line.split()
            name = parts[0]
            weight = int(parts[1][1:-1])
            d = None
            if name in disks:
                d = disks[name]
                d.weight = weight
            else:
                d = Disk(name, weight)
                disks[name] = d
                graph[name] = d
            for pn in parts[3:]:
                pn = pn.strip(',')
                d2 = None
                if pn in disks:
                    d2 = disks[pn]
                    del graph[pn]
                else:
                    d2 = Disk(pn, -1)
                disks[pn] = d2
                d.children[pn] = d2
        else:
            parts = line.split()
            name = parts[0]
            weight = int(parts[1][1:-1])
            if name in disks:
                disks[name].weight = weight
            else:
                d = Disk(name, weight)
                disks[name] = d
                graph[name] = d
    return list(graph.values())[0]

def bottom(graph):
    return graph.name

def _sum_parts(node):
    if len(node.children.values()) == 0:
        return node.weight
    node.childrensum = sum([_sum_parts(x) for x in node.children.values()])
    return node.weight + node.childrensum

def inbalance(graph):
    _sum_parts(graph)
    cur = graph
    delta = 0
    common = 0
    while True:
        children = {}
        for child in cur.children:
            c = cur.children[child]
            children[child] = c.weight + c.childrensum
        (out, common) = _outlier(children)
        if delta != 0 and not out:
            return cur.weight + delta
        delta = common - children[out]
        cur = cur.children[out]
    return 0

def _outlier(nodes):
    counts = {}
    for k in nodes:
        if nodes[k] in counts:
            counts[nodes[k]] += 1
        else:
            counts[nodes[k]] = 1

    if len(counts.values()) == 1:
        return (None, None)
    Min = min(counts.values())
    Max = max(counts.values())

    for v in counts:
        c = counts[v]
        if c == Max:
            common = v
            break
    for v in counts:
        c = counts[v]
        if c == Min:
            n = v
            break
    for i in nodes:
        if nodes[i] == v:
            return i, common
    return (None, None)

if __name__ == "__main__":
    g = build_graph(sample)
    assert(_outlier({'a':1, 'b':2, 'c':1}) == ('b', 1))
    assert(bottom(g) == "tknk")
    assert(inbalance(g) == 60)
    with open("7_in.txt") as f:
        txt = f.read()
        g2 = build_graph(txt)
        print("Part 1: %s" % bottom(g2))
        print("Part 2: %s" % inbalance(g2))
