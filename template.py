#!/usr/bin/env python3

def part1(in_txt):
    return 0

def part2(in_txt):
    return 0

if __name__ == "__main__":
    sample = ""
    assert(part1(sample) == 0)
    assert(part2(sample) == 0)
    with open("18_in.txt") as f:
        in_txt = f.read().strip()
        print("Part 1: {0}".format(part1(in_txt)))
        print("Part 2: {0}".format(part2(in_txt)))
