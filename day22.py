#!/usr/bin/env python3

clockorder = ['r','d','l','u']
reverse = {'l':'r', 'r':'l', 'u':'d', 'd':'u'}
directions = {'r': (1,0), 'd': (0,1), 'l': (-1,0), 'u': (0,-1)}
right = lambda d: clockorder[(clockorder.index(d) + 1) % len(clockorder)]
left = lambda d: clockorder[(clockorder.index(d) - 1) % len(clockorder)]
move2 = {'#':right, 'W': lambda x: x, '.': left, 'F': lambda d: reverse[d]}

def build_graph(in_txt):
    g = {}
    lines = in_txt.split('\n')
    i,j = -1*(len(lines) // 2), -1*(len(lines) // 2)
    starti,startj = i,j
    for l in lines:
        g[j] = {}
        for c in list(l):
            g[j][i] = c
            i += 1
        j += 1
        i = starti
    return g

def part1(in_txt):
    direction = 'u'
    count = 0
    g = build_graph(in_txt)
    lines = in_txt.split('\n')
    i,j = -1*(len(lines) // 2), -1*(len(lines) // 2)
    i,j = 0, 0
    for _ in range(10000):
        if j not in g:
            g[j] = {}
        if i not in g[j]:
            g[j][i] = '.'

        if g[j][i] == '#':
            direction = right(direction)
            g[j][i] = '.'
        else:
            direction = left(direction)
            g[j][i] = '#'
            count += 1
        i,j = map(sum, zip((i,j), directions[direction]))
    return count

def part2(in_txt, itercount):
    direction = 'u'
    next_state = {'.':'W', 'W':'#', '#':'F', 'F':'.'}
    count = 0
    g = build_graph(in_txt)
    i,j = 0,0
    for _ in range(itercount):
        if j not in g:
            g[j] = {}
        if i not in g[j]:
            g[j][i] = '.'
        direction = move2[g[j][i]](direction)
        g[j][i] = next_state[g[j][i]]
        if g[j][i] == '#':
            count += 1
        i,j = map(sum, zip((i,j), directions[direction]))
    return count

if __name__ == "__main__":
    sample = """..#\n#..\n..."""
    assert(part1(sample) == 5587)
    assert(part2(sample, 100) == 26)
    assert(part2(sample, 10000000) == 2511944)
    with open("22_in.txt") as f:
        in_txt = f.read().strip()
        p1 = part1(in_txt)
        print("Part 1: {0}".format(p1))
        assert(p1 == 5223)
        p2 = part2(in_txt, 10000000)
        print("Part 2: {0}".format(part2(p2)))
        assert(p2 == 2511456)
