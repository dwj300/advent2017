#!/usr/bin/env python3
sample = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

def calc(instructions, Max=False):
    m = 0
    registers = {}
    for instruction in instructions:
        parts = instruction.split(' ')
        r = parts[0]
        if r not in registers:
            registers[r] = 0
        r2 = parts[4]
        cond = parts[5]
        val = int(parts[6])
        should_update = False
        if r2 not in registers:
            registers[r2] = 0
        if cond == '>':
            should_update = registers[r2] > val
        elif cond == '<':
            should_update = registers[r2] < val
        elif cond == '>=':
            should_update = registers[r2] >= val
        elif cond == '<=':
            should_update = registers[r2] <= val
        elif cond == '==':
            should_update = registers[r2] == val
        elif cond == '!=':
            should_update = registers[r2] != val
        if should_update:
            if parts[1] == "inc":
                registers[r] += int(parts[2])
            else: 
                registers[r] -= int(parts[2])
            if registers[r] > m:
                m = registers[r]
    if Max:
        return m
    else:
        return max(registers.values()) 

def calc2(instructions):
    return calc(instructions, True)

if __name__ == "__main__":
    assert(calc(sample.split('\n')) == 1)
    assert(calc2(sample.split('\n')) == 10)
    with open("8_in.txt") as f:
        instructions = f.readlines()
        print("Part 1: {0}".format(calc(instructions)))
        print("Part 2: {0}".format(calc2(instructions)))
