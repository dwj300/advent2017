#!/usr/bin/env python3
from functools import reduce

def part1(ls, l):
    s = compute(ls, l)
    return s[0] * s[1]

def compute(list_size, lengths, rounds=1):
    nums = list(range(list_size))
    cur = 0
    skip = 0
    for r in range(rounds):
        for l in lengths:
            end = cur + l
            if end >= list_size:
                part1 = nums[cur:]
                part2 = nums[0:(end-list_size)]
                part1.extend(part2)
                part1.reverse()
                nums[cur:] = part1[:list_size-cur]
                nums[0:(end-list_size)] = part1[list_size-cur:]
            else:
                temp = nums[cur:cur+l]
                temp.reverse()
                nums[cur:cur+l] = temp
            cur = (cur + l + skip) % list_size
            skip += 1
    return nums

def strhash(seq):
    seq = list(map(ord, seq))
    seq.extend([17, 31, 73, 47, 23])
    nums = compute(256, seq, 64)
    out = ""
    for i in range(16):
        t = reduce(lambda x,y: x^y, nums[16*i:16*(i+1)])
        h = hex(t)
        out += "0" + h[2:] if len(h) == 3 else h[2:]
    return out

if __name__ == "__main__":
    assert(part1(5, [3,4,1,5]) == 12)
    assert(strhash("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert(strhash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd")
    assert(strhash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d")
    assert(strhash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e")
    with open("10_in.txt") as f:
        seq = list(map(int, f.read().strip().split(',')))
        print("Part 1: {0}".format(part1(256, seq)))
        f.seek(0)
        chars = f.read().strip()
        print("Part 2: {0}".format(strhash(chars)))
