#!/usr/bin/env python3
from functools import reduce
from day10 import *

def part1(in_txt):
    return sum(map(lambda i: calc("{0}-{1}".format(in_txt, i)).count('1'), range(128)))

def calc(knot):
    return "".join(list(map(lambda c: "{:04b}".format(int(c,16)), strhash(knot))))

def part2(in_txt):
    a = [[int(j) for j in calc("{0}-{1}".format(in_txt, i))] for i in range(128)]
    c = 0
    colors = {}
    for i in range(128):
        for j in range(128):
            color(a, i, j, colors, c)
            c += 1
    return len(set(colors.values()))

def color(a, x, y, colors, c):
    if x < 0 or x >= 128 or y < 0 or y >= 128:
        return
    if a[x][y] == 0 or (x,y) in colors:
        return
    colors[(x,y)] = c
    for (i,j) in [(1,0),(-1,0),(0,1),(0,-1)]:
        color(a,x+i,y+j,colors,c)

if __name__ == "__main__":
    sample = "flqrgnkx"
    assert(part1(sample) == 8108)
    assert(part2(sample) == 1242)
    in_txt = "jzgqcdpd"
    print("Part 1: {0}".format(part1(in_txt)))
    print("Part 2: {0}".format(part2(in_txt)))

