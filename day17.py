#!/usr/bin/env python3
def cycle(steps):
    buf = [0]
    cur = 0
    for i in range(1, 2018):
        cur = (cur + steps) % len(buf)
        buf.insert(cur+1, i)
        cur += 1
    return buf[(buf.index(2017)+1)%len(buf)]

def part2(steps):
    cur, second = 0, 0
    for i in range(1, 50000001):
        cur = 1 + (cur + steps) % i
        if cur == 1:
            second = i
    return second

if __name__ == '__main__':
    assert(cycle(3) == 638)
    part1 = cycle(344)
    print("Part 1: {0}".format(part1))
    assert(part1 == 996)
    part2 = part2(344)
    print("Part 2: {0}".format(part2))
    assert(part2 == 1898341)
