#!/usr/bin/env python3

def helper(cur, bridge, options):
    next_steps = list(filter(lambda x: x[0] == cur or x[1] == cur, options))
    if (len(next_steps) == 0):
        return sum(map(lambda x: x[0]+x[1], bridge))
    return max(map(lambda x: helper(x[0] if x[1] == cur else x[1], bridge + [x], [j for j in options if j != x]), next_steps))

def part1(in_txt):
    components = [(int(l.split('/')[0]), int(l.split('/')[1])) for l in in_txt.split('\n')]
    return helper(0, [], components)

def helper2(cur, bridge, options):
    next_steps = list(filter(lambda x: x[0] == cur or x[1] == cur, options))
    if (len(next_steps) == 0):
        return [bridge]
    bridges = []
    for x in next_steps:
        bridges.extend(helper2(x[0] if x[1] == cur else x[1], bridge + [x], [j for j in options if j != x]))
    return bridges

def part2(in_txt):
    components = [(int(l.split('/')[0]), int(l.split('/')[1])) for l in in_txt.split('\n')]
    bridges = helper2(0, [], components)
    max_l = max(map(len, bridges))
    bridges2 = list(filter(lambda x: len(x) == max_l, bridges))
    bridge = max(bridges2, key=lambda y: sum(map(lambda x: x[0]+x[1], y)))
    return sum(map(lambda x: x[0]+x[1], bridge))

if __name__ == "__main__":
    sample = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
    p1 = part1(sample)
    print(p1)
    assert(p1 == 31)
    p2 = part2(sample)
    print(p2)
    assert(p2 == 19)
    with open("24_in.txt") as f:
        in_txt = f.read().strip()
        print("Part 1: {0}".format(part1(in_txt)))
        print("Part 2: {0}".format(part2(in_txt)))
