#!/usr/bin/env python3
from math import *

def distance(n):
    sl = int(ceil(sqrt(n)))
    if sl % 2 == 0:
        sl += 1
    offset = int((sl - 1.0) / 2.0)
    corners = list(map(lambda x: (sl*sl - (x * (sl - 1))), range(4)))
    midpts = list(map(lambda x: (sl*sl - (offset + x*(sl - 1))), range(4)))
    a = 0
    b = offset + min(list(map(lambda x: abs(n-x), corners))) - offset
    options = list(map(lambda x: abs(n-x), midpts))
    other = min(options)
    dist = offset + other
    return dist

def build_grid(m):
    # todo: better bounding
    n = int(sqrt(sqrt(m)))
    grid = [[0 for _ in range(n)] for _ in range(n)]
    i = int(floor(n / 2))
    j = int(floor(n / 2))
    grid[j][i] = 1
    i += 1
    d = 'r'
    # todo: cleanup second if block
    while i != n-1 and j != n-1:
        grid[j][i] = sq_sum(grid, i, j, n-2)
        if grid[j][i] > m:
            return grid[j][i]
        if d == 'r' and grid[j-1][i] == 0:
            d = 'u'
            # j -= 1
        elif d == 'u' and grid[j][i-1] == 0:
            d = 'l'
            # i -= 1
        elif d == 'l' and grid[j+1][i] == 0:
            d = 'd'
            # j += 1
        elif d == 'd' and grid[j][i+1] == 0:
            d = 'r'
            # i += 1
        #"""
        if d == 'r': i += 1
        elif d == 'u': j -= 1
        elif d == 'l': i -= 1
        elif d == 'd': j += 1
        #"""
    return -1

def sq_sum(grid, i, j, n):
    s = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            try:
                s += grid[y][x]
            except:
                pass
    return s

if __name__ == '__main__':
    assert(distance(1) == 0)
    assert(distance(12) == 3)
    assert(distance(23) == 2)
    assert(distance(1024) == 31)
    print("Part 1: {0}".format(distance(289326)))
    print("Part 2: {0}".format(build_grid(289326)))
