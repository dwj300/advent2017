#!/usr/bin/env python3
import string

def part1(moves, seq):
    def spin(s, m, l): s[l:], s[:l] = s[:l-int(m)], s[l-int(m):]
    def swap_pos(seq, move, size): swap(seq, move, int)
    def swap_name(seq, move, size): swap(seq, move, lambda x: seq.index(x))
    def swap(seq, move, func): doswap(seq, tuple(map(func, move.split('/'))))
    def doswap(seq, ab): seq[ab[0]], seq[ab[1]] = seq[ab[1]], seq[ab[0]]
    dances = {'s': spin, 'x': swap_pos, 'p': swap_name}
    list(map(lambda move: dances[move[0]](seq, move[1:], len(seq)), moves))
    return "".join(seq)

def part2(moves, seq, n):
    seen = set()
    hist = []
    for i in range(n):
        t = tuple(seq)
        if t in seen:
            return ''.join(hist[n % len(seen)])
        seen.add(t)
        hist.append(t)
        part1(moves, seq)
    return ''.join(seq)

if __name__ == "__main__":
    sample = ['s1', 'x3/4','pe/b']
    assert(part1(sample, list(string.ascii_lowercase)[:5]) == "baedc")
    assert(part2(sample, list(string.ascii_lowercase)[:5], 2) == "ceadb")
    with open("16_in.txt") as f:
        moves = f.read().strip().split(',')
    part1ans = part1(moves,list(string.ascii_lowercase)[:16])
    print("Part 1: {0}".format(part1ans))
    assert(part1ans == "bijankplfgmeodhc")
    part2ans = part2(moves,list(string.ascii_lowercase)[:16], 1000000000)
    print("Part 2: {0}".format(part2ans))
    assert(part2ans == "bpjahknliomefdgc")
