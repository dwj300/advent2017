#!/usr/bin/env python3

def part1(a, b):
    count = 0
    for i in range(40000000):
        a *= 16807
        b *= 48271
        a = a % 2147483647
        b = b % 2147483647
        sa = "{0:b}".format(a)[-16:]
        sb = "{0:b}".format(b)[-16:]
        if sa == sb:
            count += 1
    return count

def part2(a, b):
    count = 0
    for i in range(5000000):
        a *= 16807
        a = a % 2147483647
        while a % 4 != 0:
            a *= 16807
            a = a % 2147483647
        b *= 48271
        b = b % 2147483647
        while b % 8 != 0:
            b *= 48271
            b = b % 2147483647
        sa = "{0:b}".format(a)[-16:]
        sb = "{0:b}".format(b)[-16:]
        if sa == sb:
            count += 1
    return count

if __name__ == "__main__":
    assert(part1(65, 8921) == 588)
    assert(part2(65, 8921) == 1242)
    print("Part 1: {0}".format(part1(512, 191)))
    print("Part 2: {0}".format(part2(512, 191)))

