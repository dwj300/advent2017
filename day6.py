#!/usr/bin/env python3
def num_cycles(banks):
    cycles = 0
    length = 0
    states = set()
    states.add(tuple(banks))   
    while True:
        redistribute(banks)
        cycles += 1
        if tuple(banks) in states:
            return cycles
        else:
            states.add(tuple(banks))

def redistribute(banks):
    m = max(banks)
    indices = [i for i,x in enumerate(banks) if x == m]
    i = min(indices)
    cur = banks[i]
    banks[i] = 0
    while cur > 0:
        i = (i + 1) % len(banks)
        banks[i] += 1
        cur -= 1
    return banks

def num_cycles2(banks):
    seen = {tuple(banks):0}
    cycles = 0
    length = 0
    while True:
        redistribute(banks)
        cycles += 1
        if tuple(banks) in seen:
            return cycles - seen[tuple(banks)]
        seen[tuple(banks)] = cycles

if __name__ == '__main__':
    assert(num_cycles([0,2,7,0]) == 5)
    with open("6_in.txt") as f:
        ints = [int(i) for i in f.read().strip().split()]
        print("Part 1: {0}".format(num_cycles(ints)))
        print("Part 2: {0}".format(num_cycles2(ints)))

