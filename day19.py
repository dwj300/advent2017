#!/usr/bin/env python3
from itertools import count

def traverse(in_txt):
    dirs = {'d': (0,1), 'u': (0,-1), 'l':(-1,0), 'r':(1,0)}
    graph = [[i for i in list(j)] for j in in_txt.split('\n')]
    cur_dir, seen = 'd', ""
    i, j = graph[0].index('|'), 0
    for c in count():
        char = graph[j][i]
        if char == '|' or char == '-':
            i,j = [sum(x) for x in zip((i,j), dirs[cur_dir])]
        elif char == '+':
            check = ['d', 'u']
            if cur_dir in ['d', 'u']:
                check = ['l', 'r']
            for o in check:
                ti,tj = i + dirs[o][0], j + dirs[o][1]
                if ti >= 0 and ti < len(graph[0]) and tj >= 0 and tj < len(graph) and graph[tj][ti] != ' ':
                    i,j = ti,tj
                    cur_dir = o
                    break
        elif char != ' ':
            seen += graph[j][i]
            i,j = [sum(x) for x in zip((i,j), dirs[cur_dir])]
        else:
            return seen, c

if __name__ == "__main__":
    sample = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """
    assert(traverse(sample)[0] == "ABCDEF")
    assert(traverse(sample)[1] == 38)
    with open("19_in.txt") as f:
        in_txt = f.read()
        p1, p2 = traverse(in_txt)
        print("Part 1: {0}".format(p1))
        print("Part 2: {0}".format(p2))
        assert(p1 == "MOABEUCWQS")
        assert(p2 == 18058)
