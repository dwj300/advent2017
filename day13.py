#!/usr/bin/env python3
import copy
from itertools import count

def severity(text):
    weights = _parse_input(text)
    penalty = 0
    cur = 0 
    m = max(weights.keys())
    while cur <= m:
        if cur in weights and weights[cur][1] == 0:
            penalty += weights[cur][0] * cur
        cur += 1
        _dostep(weights) 
    return penalty

def _dostep(weights, num=1):
    for _ in range(num):
        for k in weights.keys():
            v = weights[k]
            d = v[2]
            if v[1] == v[0] - 1:
                d = -1
                weights[k][2] = d
            elif v[1] == 0:
                d = 1
                weights[k][2] = d
            weights[k][1] = v[1] + d

def _parse_input(text):
    weights = {}
    for l in text.split('\n'):
        parts = l.split(":")
        weights[int(parts[0])] = [int(parts[1].strip()), 0, 1]
    return weights

def caught(weights, delay):
    for t in weights.items():
        if (delay+t[0]) % ((t[1][0]-1)*2) == 0:
            return True
    return False

def delay2(text):
    weights = _parse_input(text)
    i = 0
    while True:
        if caught(weights, i):
            i += 1
        else:
            return i

if __name__ == "__main__":
    sample = """0: 3
1: 2
4: 4
6: 4"""
    assert(severity(sample) == 24)
    assert(delay2(sample) == 10)
    with open("13_in.txt") as f:
        txt = f.read().strip()
        print("Part 1: {0}".format(severity(txt)))
        print("Part 2: {0}".format(delay2(txt)))
