#!/usr/bin/env python3
from itertools import product
from day10 import strhash

def part1(in_txt):
    return sum(map(lambda i: calc("{0}-{1}".format(in_txt, i)).count('1'), range(128)))

def calc(knot):
    return "".join(list(map(lambda c: "{:04b}".format(int(c,16)), strhash(knot))))

def part2(in_txt):
    colors = {}
    a = [[int(j) for j in calc("{0}-{1}".format(in_txt, i))] for i in range(128)]
    list(map(lambda t: color(a, t[1][0], t[1][1], colors, t[0]), enumerate(product(range(128), range(128)))))
    return len(set(colors.values()))

def color(a, x, y, colors, c):
    if x < 0 or x >= 128 or y < 0 or y >= 128 or a[x][y] == 0 or (x,y) in colors: return
    colors[(x,y)] = c
    list(map(lambda t: color(a,x+t[0],y+t[1],colors,c), [(1,0),(-1,0),(0,1),(0,-1)])) 

if __name__ == "__main__":
    sample = "flqrgnkx"
    assert(part1(sample) == 8108)
    assert(part2(sample) == 1242)
    in_txt = "jzgqcdpd"
    print("Part 1: {0}".format(part1(in_txt)))
    print("Part 2: {0}".format(part2(in_txt)))

