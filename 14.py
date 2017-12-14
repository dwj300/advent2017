import binascii
import numpy as np
from scipy.ndimage.measurements import label
from functools import reduce
a = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
def part1(in_txt):
    used = 0
    for i in range(128):
        used += calc("{0}-{1}".format(in_txt, i)).count('1')
    return used

def calc(knot):
    hexstr = strhash(knot)
    binstr = ""
    for c in hexstr:
        pos = a.index(c)
        b = "{:04b}".format(pos)
        binstr += b
    return binstr

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

def part2(in_txt):
    a = []
    for i in range(128):
        a.append([int(i) for i in calc("{0}-{1}".format(in_txt, i))])
    #print(a)
    arr = np.array(a)
    structure = np.array([[0,1,0],[1,1,1],[0,1,0]])
    labeled, ncomponents = label(arr, structure)
    return ncomponents

if __name__ == "__main__":
    calc("")
    sample = "flqrgnkx"
    assert(part1(sample) == 8108)
    assert(part2(sample) == 1242)
    #with open("14_in.txt") as f:
    in_txt = "jzgqcdpd"
    print("Part 1: {0}".format(part1(in_txt)))
    print("Part 2: {0}".format(part2(in_txt)))

